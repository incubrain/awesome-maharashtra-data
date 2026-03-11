#!/usr/bin/env python3
"""
Direct metadata generation runner - works within Claude Code environment.
"""

import os
import sys
import json
import time
import yaml
from pathlib import Path
from typing import Optional, Dict, Any

# Import after ensuring packages are available
import anthropic

def parse_catalog():
    """Parse CATALOG.md and extract first N datasets."""
    catalog_path = Path(__file__).parent.parent / "CATALOG.md"
    datasets = []

    with open(catalog_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_table = False
    for line in lines:
        if line.startswith("|"):
            if not in_table and any(x in line for x in ["Category", "Dataset"]):
                in_table = True
                continue

            if in_table and line.strip() != "|" and "---" not in line:
                parts = [p.strip() for p in line.split("|")[1:-1]]
                if len(parts) >= 5 and not parts[0].startswith("--"):
                    try:
                        num, category, dataset, modality, license_str = parts[0], parts[1], parts[2], parts[3], parts[4]
                        if num and category and dataset:
                            slug = dataset.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("_", "-")
                            datasets.append({
                                'title': dataset,
                                'slug': slug,
                                'category': category,
                                'modality': modality,
                                'license': license_str
                            })
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

def generate_metadata(client: anthropic.Anthropic, dataset: Dict[str, Any], existing: Optional[Dict] = None) -> Dict[str, Any]:
    """Generate metadata using Claude."""

    context = ""
    if existing and existing.get("description"):
        context += f"Description: {existing['description']}\n"
    if existing and existing.get("homepage"):
        context += f"Homepage: {existing['homepage']}\n"

    prompt = f"""Generate metadata for this dataset in valid JSON format only (no markdown).

Dataset: {dataset['title']}
Category: {dataset['category']}
Modality: {dataset['modality']}
License: {dataset['license']}

{context}

Return ONLY this JSON structure with no extra text:
{{
  "schema": [
    {{"field": "field_name", "type": "string|int|float|date|boolean|json", "description": "description"}}
  ],
  "starter_idea": "One specific idea for a Marathi developer/entrepreneur",
  "build_ideas": [
    "First detailed, specific idea",
    "Second idea solving a real problem",
    "Third idea with ML/AI"
  ],
  "quick_start": "3-4 lines of runnable Python code"
}}"""

    try:
        response = client.messages.create(
            model="claude-opus-4-6-20250514",  # Latest model
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = response.content[0].text.strip()

        # Try to parse JSON
        try:
            if response_text.startswith("```"):
                response_text = response_text.split("```")[1]
                if response_text.startswith("json"):
                    response_text = response_text[4:]
            return json.loads(response_text)
        except json.JSONDecodeError:
            print(f"  Warning: Failed to parse JSON response", file=sys.stderr)
            return {}
    except Exception as e:
        print(f"  API Error: {e}", file=sys.stderr)
        return {}

def save_yaml(dataset_slug: str, metadata: Dict[str, Any]) -> bool:
    """Save metadata to YAML."""
    yaml_path = Path(__file__).parent.parent / "data_cards" / f"{dataset_slug}.yaml"

    try:
        class CustomDumper(yaml.SafeDumper):
            pass

        def str_presenter(dumper, data):
            if '\n' in data:
                return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
            return dumper.represent_scalar('tag:yaml.org,2002:str', data)

        CustomDumper.add_representer(str, str_presenter)

        yaml_str = yaml.dump(metadata, Dumper=CustomDumper,
                            default_flow_style=False, allow_unicode=True, sort_keys=False)

        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        with open(yaml_path, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write(yaml_str)

        print(f"✓ Saved {yaml_path.name}")
        return True
    except Exception as e:
        print(f"✗ Error saving {yaml_path}: {e}", file=sys.stderr)
        return False

def main():
    print("🚀 Starting Metadata Generation for Marathi Datasets\n")

    # Initialize Anthropic client
    try:
        client = anthropic.Anthropic()
        print("✓ Anthropic client initialized")
    except Exception as e:
        print(f"✗ Failed to initialize Anthropic client: {e}")
        print("Make sure ANTHROPIC_API_KEY is set")
        sys.exit(1)

    # Parse datasets
    datasets = parse_catalog()
    print(f"✓ Found {len(datasets)} datasets in CATALOG.md\n")

    # Process first 10 as demo
    datasets = datasets[:10]
    print(f"Processing first {len(datasets)} datasets...\n")

    processed = 0
    skipped = 0
    errors = 0

    for idx, dataset in enumerate(datasets, 1):
        print(f"[{idx}/{len(datasets)}] {dataset['title']}")

        # Load existing
        existing = get_existing_yaml(dataset['slug'])

        # Check if complete
        if existing and all(existing.get(k) for k in ['schema', 'starter_idea', 'build_ideas', 'quick_start']):
            print(f"  ↷ Already complete, skipping")
            skipped += 1
            continue

        # Generate
        print(f"  → Generating metadata...")
        generated = generate_metadata(client, dataset, existing)

        if not generated:
            print(f"  ✗ Failed to generate")
            errors += 1
            continue

        # Merge
        if existing:
            merged = {**existing, **generated}
        else:
            merged = {
                "title": dataset['title'],
                "category": dataset['category'],
                "modality": dataset['modality'],
                "license": dataset['license'],
                **generated
            }

        # Save
        if save_yaml(dataset['slug'], merged):
            processed += 1
        else:
            errors += 1

        time.sleep(0.5)  # Rate limiting

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✓ Processed: {processed}")
    print(f"  ↷ Skipped:   {skipped}")
    print(f"  ✗ Errors:    {errors}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
