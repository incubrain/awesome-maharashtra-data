# Contributing

Thank you for helping build the definitive catalog of Maharashtra and Marathi public datasets. Every contribution makes it easier for innovators to build AI-powered solutions for agriculture, governance, healthcare, and beyond.

Browse the full catalog at **[data.incubrain.org](https://data.incubrain.org)**.

## What Qualifies

- Dataset must be **publicly accessible** (no login-wall or paywall-only).
- Must contain **Marathi language data** OR **Maharashtra-specific data**.
- Must have a **working download link** or documented API endpoint.
- Must be **openly licensed** (CC-BY, CC0, ODbL, MIT, government open data). Proprietary-with-free-tier accepted only if clearly noted.
- No scraped data from sites that prohibit it. No paid APIs.

## How to Add a Dataset

### Quick (open an issue)

Use the "Add Dataset" issue template. Provide:

- Dataset name and URL
- One-line description
- License (or "Unknown")
- Approximate size

### Full (pull request)

1. Fork this repo.
2. Add a new YAML file under `content/datasets/<dataset-slug>.yaml` with all required metadata fields.
3. Submit PR with title: `Add <Dataset Name>`.

## Quality Standards

- Description starts with uppercase, ends with period.
- Link must be direct (no URL shorteners, no Google Drive redirect links).
- No duplicates (search existing entries first).
- License **must** be specified. If unknown, note "Unknown - verify before commercial use".
- Size in standard units: tokens, sentences, hours, images, rows, or bytes (MB/GB).
- Every entry must include at least one AI use case.

## What Gets Rejected

- Broken or inaccessible links.
- Datasets with unclear or restrictive licensing (unless clearly flagged).
- Duplicates of existing entries.
- Entries missing required metadata (name, URL, license, description).
- Scraped datasets that violate source terms of service.

## Code of Conduct

Be respectful and constructive. We follow the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
