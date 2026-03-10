#!/usr/bin/env python3
"""
filter_datagov.py — Search and filter Maharashtra datasets from data.gov.in API.

Usage:
    python filter_datagov.py --query "crop production" --limit 10
    python filter_datagov.py --query "maharashtra agriculture" --format csv

Requires: requests (pip install requests)
"""

import argparse
import json
import sys

try:
    import requests
except ImportError:
    print("Install requests: pip install requests", file=sys.stderr)
    sys.exit(1)

BASE_URL = "https://data.gov.in/backend/dmspublic/v1/resources"
MAHARASHTRA_KEYWORDS = ["maharashtra", "mumbai", "pune", "nagpur", "nashik"]


def search_datasets(query: str, limit: int = 20, offset: int = 0) -> dict:
    """Search data.gov.in catalog for datasets matching query."""
    params = {
        "filters[title]": query,
        "offset": offset,
        "limit": limit,
        "sort[changed]": "desc",
    }
    resp = requests.get(BASE_URL, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def filter_maharashtra(results: list) -> list:
    """Filter results to Maharashtra-relevant entries."""
    filtered = []
    for item in results:
        title = (item.get("title") or "").lower()
        desc = (item.get("field_description") or "").lower()
        combined = title + " " + desc
        if any(kw in combined for kw in MAHARASHTRA_KEYWORDS):
            filtered.append(item)
    return filtered


def display_results(results: list, fmt: str = "table") -> None:
    """Display search results."""
    if fmt == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    if not results:
        print("No results found.")
        return

    print(f"\n{'#':<4} {'Title':<60} {'Format':<8} {'Org':<30}")
    print("-" * 105)
    for i, item in enumerate(results, 1):
        title = (item.get("title") or "N/A")[:58]
        fmt_str = (item.get("field_resource_file_type") or "N/A")[:6]
        org = (item.get("field_api_source_title") or "N/A")[:28]
        print(f"{i:<4} {title:<60} {fmt_str:<8} {org:<30}")


def main():
    parser = argparse.ArgumentParser(description="Search Maharashtra datasets on data.gov.in")
    parser.add_argument("--query", "-q", required=True, help="Search query")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max results (default: 20)")
    parser.add_argument("--format", "-f", choices=["table", "json"], default="table", help="Output format")
    parser.add_argument("--mh-only", action="store_true", help="Filter to Maharashtra-specific results")
    args = parser.parse_args()

    print(f"Searching data.gov.in for: {args.query}")
    data = search_datasets(args.query, limit=args.limit)

    results = data.get("results", data.get("records", []))
    if not isinstance(results, list):
        results = []

    if args.mh_only:
        results = filter_maharashtra(results)
        print(f"Filtered to {len(results)} Maharashtra-specific results")

    display_results(results, args.format)


if __name__ == "__main__":
    main()
