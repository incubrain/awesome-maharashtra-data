# Contributing

Thank you for helping build the definitive catalog of Maharashtra and Marathi public datasets. Every contribution makes it easier for innovators to build AI-powered solutions for agriculture, governance, healthcare, and beyond.

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
2. Copy `data_cards/_template.yaml` to `data_cards/<dataset-slug>.yaml` and fill in all fields.
3. Add the entry row to the matching `categories/<nn>-<name>.md` table.
4. Add a bulleted entry to the matching section in `README.md`.
5. Submit PR with title: `Add <Dataset Name>`.

## Entry Formats

### Bulleted entry in README.md

```markdown
- [Dataset Name](URL) - Description ending with period. `Modality` `License`
```

Example:

```markdown
- [L3Cube-MahaSent](https://huggingface.co/datasets/l3cube-pune/MahaSent) - Marathi sentiment analysis dataset with 16K tweets across 3 classes. `Text` `CC-BY-4.0`
```

Rules:
- Link first, then ` - ` (space-dash-space), then description.
- Description starts with uppercase, ends with `.`
- Modality and license as inline code tags at end.

### Table row in category file

```markdown
| **[Dataset Name](URL)** - Description. | Size | License | Modality | [HF](url) / [Paper](url) | AI Use Case |
```

Columns: Dataset (name + description merged) | Size | License | Modality | Links | AI Use Case

### YAML data card

Copy `data_cards/_template.yaml` and fill all fields. See the template for field descriptions.

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
