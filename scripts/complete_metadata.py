#!/usr/bin/env python3
"""
complete_metadata.py — Intelligently populate missing metadata for all 248+ datasets.

This script:
1. Parses CATALOG.md to extract dataset information
2. Creates/updates YAML data cards with:
   - schema: Field definitions (name, type, description)
   - starter_idea: Quick business/ML idea using this dataset
   - build_ideas: 2-3 detailed implementation ideas
   - quick_start: Code snippet to get started
   - organization: Organization/author
   - direct_download_url: Where to download

Uses Claude Haiku (cost-efficient) for intelligent metadata generation.

Usage:
    python scripts/complete_metadata.py                    # Process all datasets
    python scripts/complete_metadata.py --dataset "ai4bharat-samanantar-mr"  # Single dataset
    python scripts/complete_metadata.py --dry-run          # Preview changes without writing
    python scripts/complete_metadata.py --start-from 50    # Resume from dataset #50
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, List, Any
from dataclasses import dataclass
import time

try:
    import yaml
except ImportError:
    print("Install PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    import anthropic
except ImportError:
    print("Install Anthropic SDK: pip install anthropic", file=sys.stderr)
    sys.exit(1)


@dataclass
class DatasetInfo:
    """Dataset information from CATALOG.md."""
    title: str
    category: str
    modality: str
    license: str
    ai_use_case: str
    slug: Optional[str] = None
    description: Optional[str] = None


def parse_catalog() -> List[DatasetInfo]:
    """Parse CATALOG.md and extract dataset entries."""
    catalog_path = Path(__file__).parent.parent / "CATALOG.md"

    if not catalog_path.exists():
        print(f"Error: CATALOG.md not found at {catalog_path}", file=sys.stderr)
        sys.exit(1)

    datasets = []
    with open(catalog_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Skip header lines until we find the table
    in_table = False
    for line in lines:
        if line.startswith("|"):
            if not in_table and any(x in line for x in ["Category", "Dataset", "Modality"]):
                in_table = True
                continue

            if in_table and line.strip() != "|" and "---" not in line:
                # Parse table row: | # | Category | Dataset | Modality | License | AI Use Case |
                parts = [p.strip() for p in line.split("|")[1:-1]]
                if len(parts) >= 5 and not parts[0].startswith("--"):
                    try:
                        num, category, dataset, modality, license_str, ai_use = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5] if len(parts) > 5 else ""
                        if num and category and dataset:
                            # Generate slug from dataset name
                            slug = dataset.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("_", "-")
                            slug = re.sub(r'[^a-z0-9\-]', '', slug)
                            slug = re.sub(r'-+', '-', slug).strip('-')

                            datasets.append(DatasetInfo(
                                title=dataset,
                                category=category,
                                modality=modality,
                                license=license_str,
                                ai_use_case=ai_use,
                                slug=slug
                            ))
                    except (IndexError, ValueError):
                        pass

    return datasets


def get_existing_yaml(dataset_slug: str) -> Optional[Dict[str, Any]]:
    """Load existing YAML if it exists."""
    yaml_path = Path(__file__).parent.parent / "data_cards" / f"{dataset_slug}.yaml"

    if not yaml_path.exists():
        return None

    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Warning: Could not load {yaml_path}: {e}", file=sys.stderr)
        return None


def generate_metadata_with_claude(
    client: anthropic.Anthropic,
    dataset_info: DatasetInfo,
    existing_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Use Claude Haiku to generate missing metadata fields."""

    # Build context for Claude
    existing_fields = ""
    if existing_data:
        if existing_data.get("description"):
            existing_fields += f"Description: {existing_data['description']}\n"
        if existing_data.get("homepage"):
            existing_fields += f"Homepage: {existing_data['homepage']}\n"
        if existing_data.get("format"):
            existing_fields += f"Format: {existing_data['format']}\n"
        if existing_data.get("size"):
            existing_fields += f"Size: {existing_data['size']}\n"

    prompt = f"""You are a data expert for Marathi AI/ML projects. Generate metadata for this dataset.

Dataset: {dataset_info.title}
Category: {dataset_info.category}
Modality: {dataset_info.modality}
License: {dataset_info.license}
Primary Use Case: {dataset_info.ai_use_case}

{existing_fields}

Generate ONLY valid JSON (no markdown, no extra text) with these exact keys:

{{
  "schema": [
    {{"field": "field_name", "type": "data_type", "description": "what this field contains"}}
  ],
  "starter_idea": "One sentence idea for a Marathi entrepreneur or developer to build with this dataset (e.g., 'Build a crop price SMS alert app')",
  "build_ideas": [
    "First detailed idea with specific use case for Marathi/Maharashtra context",
    "Second idea focused on solving a real problem",
    "Third idea involving AI/ML application"
  ],
  "quick_start": "3-4 lines of Python code to load and explore the dataset (if tabular/text). Focus on actual tools (pandas, datasets library, etc). Make it runnable."
}}

Schema should have 3-5 key fields. Be specific to the dataset modality and content.
Build ideas should be practical and specific to Maharashtra/Marathi context.
Quick start code should be executable and use real libraries.
Starter idea should be compelling for entrepreneurs.
"""

    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract JSON from response
    response_text = response.content[0].text.strip()

    # Try to parse JSON
    try:
        # Handle markdown code blocks
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]

        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"Warning: Failed to parse Claude response for {dataset_info.title}: {e}", file=sys.stderr)
        print(f"Response was: {response_text[:200]}", file=sys.stderr)
        return {}


def merge_metadata(
    existing: Optional[Dict[str, Any]],
    generated: Dict[str, Any]
) -> Dict[str, Any]:
    """Merge existing and generated metadata."""
    if not existing:
        return generated

    # Keep existing fields, add new generated ones
    merged = existing.copy()

    # Add generated fields if they don't exist
    for key in ["schema", "starter_idea", "build_ideas", "quick_start"]:
        if key in generated and (key not in merged or not merged[key]):
            merged[key] = generated[key]

    return merged


def save_yaml(
    dataset_slug: str,
    metadata: Dict[str, Any],
    dry_run: bool = False
) -> bool:
    """Save metadata to YAML file."""
    yaml_path = Path(__file__).parent.parent / "data_cards" / f"{dataset_slug}.yaml"

    if dry_run:
        print(f"[DRY RUN] Would save to {yaml_path}")
        return True

    try:
        # Custom YAML dumper to preserve formatting
        class CustomDumper(yaml.SafeDumper):
            pass

        def str_presenter(dumper, data):
            if '\n' in data:
                return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
            return dumper.represent_scalar('tag:yaml.org,2002:str', data)

        CustomDumper.add_representer(str, str_presenter)

        yaml_str = yaml.dump(metadata, Dumper=CustomDumper,
                            default_flow_style=False, allow_unicode=True,
                            sort_keys=False)

        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        with open(yaml_path, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml_str)

        print(f"✓ Saved {yaml_path}")
        return True
    except Exception as e:
        print(f"✗ Error saving {yaml_path}: {e}", file=sys.stderr)
        return False


def get_dataset_slug_from_filename(filename: str) -> str:
    """Convert filename to dataset slug."""
    return filename.replace(".yaml", "").replace(".yml", "")


def process_datasets(
    api_key: Optional[str] = None,
    dataset_filter: Optional[str] = None,
    dry_run: bool = False,
    start_from: int = 0,
    limit: Optional[int] = None
):
    """Main processing function."""

    client = None
    if not dry_run:
        # Initialize Anthropic client - will auto-detect from env or credentials
        try:
            if api_key:
                client = anthropic.Anthropic(api_key=api_key)
            else:
                client = anthropic.Anthropic()  # Auto-detects ANTHROPIC_API_KEY from environment
        except Exception as e:
            print(f"Error: Could not initialize Anthropic client: {e}", file=sys.stderr)
            print("Make sure ANTHROPIC_API_KEY environment variable is set", file=sys.stderr)
            sys.exit(1)

    # Get all datasets from CATALOG
    datasets = parse_catalog()
    print(f"Found {len(datasets)} datasets in CATALOG.md")

    # Filter if needed
    if dataset_filter:
        datasets = [d for d in datasets if dataset_filter.lower() in d.slug.lower()]
        print(f"Filtered to {len(datasets)} datasets matching '{dataset_filter}'")

    # Apply limit if specified
    if limit:
        datasets = datasets[:limit]
        print(f"Limited to first {limit} datasets")

    # Process datasets
    processed = 0
    skipped = 0
    errors = 0

    total_datasets = len(datasets)

    for idx, dataset in enumerate(datasets[start_from:], start=start_from + 1):
        try:
            print(f"\n[{idx}/{total_datasets}] Processing: {dataset.title}")

            # Load existing YAML if it exists
            existing = get_existing_yaml(dataset.slug)

            # Check if already has advanced fields
            has_schema = existing and existing.get("schema")
            has_starter = existing and existing.get("starter_idea")
            has_build = existing and existing.get("build_ideas")
            has_quickstart = existing and existing.get("quick_start")

            if has_schema and has_starter and has_build and has_quickstart:
                print(f"  ↷ Already complete, skipping")
                skipped += 1
                continue

            # Generate missing metadata
            if dry_run:
                print(f"  → [DRY RUN] Would generate metadata with Claude Haiku")
                generated = {
                    "schema": [{"field": "example", "type": "string", "description": "Example field"}],
                    "starter_idea": "Example starter idea",
                    "build_ideas": ["Idea 1", "Idea 2", "Idea 3"],
                    "quick_start": "# Example\nprint('Loading dataset...')"
                }
            else:
                print(f"  → Generating metadata with Claude Haiku...")
                generated = generate_metadata_with_claude(client, dataset, existing)

            if not generated:
                print(f"  ✗ Failed to generate metadata")
                errors += 1
                continue

            # Merge metadata
            if existing:
                merged = merge_metadata(existing, generated)
                # Ensure core fields from existing are preserved
                merged.setdefault("title", dataset.title)
                merged.setdefault("category", dataset.category)
                merged.setdefault("modality", dataset.modality)
                merged.setdefault("license", dataset.license)
                if dataset.slug and "slug" not in merged:
                    merged["slug"] = dataset.slug
            else:
                # Create new YAML with all available info
                merged = {
                    "title": dataset.title,
                    "category": dataset.category,
                    "modality": dataset.modality,
                    "license": dataset.license,
                    "ai_use_cases": [dataset.ai_use_case] if dataset.ai_use_case else [],
                    "format": dataset.modality,
                    "update_frequency": "static",
                    "language": ["mr"],
                    **generated
                }

            # Save
            if save_yaml(dataset.slug, merged, dry_run):
                processed += 1
                time.sleep(0.2)  # Gentle rate limiting
            else:
                errors += 1

        except Exception as e:
            print(f"  ✗ Error processing {dataset.title}: {e}", file=sys.stderr)
            errors += 1
            continue

        # Progress update every 5 datasets
        if (idx - start_from) % 5 == 0:
            print(f"  ⏱ Progress: {processed} processed, {skipped} skipped, {errors} errors")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✓ Processed: {processed}")
    print(f"  ↷ Skipped:   {skipped}")
    print(f"  ✗ Errors:    {errors}")
    if dry_run:
        print("\n(DRY RUN - no files were actually written)")


def main():
    parser = argparse.ArgumentParser(
        description="Complete metadata for all Awesome Marathi Datasets",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--dataset",
        help="Process only this dataset (by slug)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files"
    )
    parser.add_argument(
        "--start-from",
        type=int,
        default=0,
        help="Resume from dataset number (for resuming interrupted runs)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Process only first N datasets (useful for testing)"
    )
    parser.add_argument(
        "--api-key",
        help="Anthropic API key (defaults to ANTHROPIC_API_KEY env var)"
    )

    args = parser.parse_args()

    process_datasets(
        api_key=args.api_key,
        dataset_filter=args.dataset,
        dry_run=args.dry_run,
        start_from=args.start_from,
        limit=args.limit
    )


if __name__ == "__main__":
    main()
