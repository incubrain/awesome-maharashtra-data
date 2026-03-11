# Quick Start: Complete Dataset Metadata

This guide shows how to run the automated metadata completion for all 172 datasets.

## Prerequisites

1. **Python 3.8+**
```bash
python3 --version
```

2. **Anthropic API Key**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

3. **Dependencies**
```bash
python3 -m pip install pyyaml anthropic
```

## Running the Script

### Option 1: Complete All Datasets (Full Run)

```bash
python3 scripts/complete_metadata.py
```

This will:
- Process all 172 datasets from CATALOG.md
- Create/update YAML files in `data_cards/`
- Generate schema, starter ideas, build ideas, and quick start code
- Show progress updates every 5 datasets
- Takes ~30-40 minutes with rate limiting

### Option 2: Test with Sample (Recommended First)

```bash
# Test with first 5 datasets
python3 scripts/complete_metadata.py --limit 5

# Test with specific dataset
python3 scripts/complete_metadata.py --dataset "samanantar"
```

### Option 3: Batch Processing with Auto-Resume

```bash
bash scripts/batch_complete_metadata.sh
```

This script:
- Processes 10 datasets at a time
- Auto-saves checkpoints (`.metadata_checkpoint`)
- Logs to `.metadata_completion.log`
- Can be resumed if interrupted: `bash scripts/batch_complete_metadata.sh`

### Option 4: Dry-Run (Preview Only)

Test without making changes:
```bash
python3 scripts/complete_metadata.py --limit 10 --dry-run
```

## Monitoring Progress

### Watch the Log

```bash
# In another terminal
tail -f .metadata_completion.log
```

### Resume from Checkpoint

If script stops:
```bash
# Batch script auto-resumes, or manually:
python3 scripts/complete_metadata.py --start-from 50
```

### Check Completion

```bash
# Count existing data cards
ls data_cards/*.yaml | wc -l

# Find incomplete cards (missing new fields)
python3 -c "
import yaml, os
from pathlib import Path
incomplete = 0
for f in Path('data_cards').glob('*.yaml'):
    if f.name == '_template.yaml': continue
    with open(f) as file:
        data = yaml.safe_load(file)
        if not all(data.get(k) for k in ['schema', 'starter_idea', 'build_ideas', 'quick_start']):
            print(f'Incomplete: {f.name}')
            incomplete += 1
print(f'\nTotal incomplete: {incomplete}')
"
```

## Example Output

```
Found 172 datasets in CATALOG.md

[1/172] Processing: L3Cube-MahaCorpus
  → Generating metadata with Claude Haiku...
✓ Saved /path/to/data_cards/l3cube-mahacorpus.yaml

[2/172] Processing: L3Cube-MahaSent-MD
  → Generating metadata with Claude Haiku...
✓ Saved /path/to/data_cards/l3cube-mahasent-md.yaml

...

[170/172] Processing: Example Dataset
  ↷ Already complete, skipping

[171/172] Processing: Another Dataset
  → Generating metadata with Claude Haiku...
✓ Saved /path/to/data_cards/another-dataset.yaml

============================================================
Summary:
  ✓ Processed: 148
  ↷ Skipped:   20  (already complete)
  ✗ Errors:    4
```

## What Gets Generated

Each dataset gets these new fields:

### `schema`
```yaml
schema:
  - field: "field_name"
    type: "string|int|float|boolean|date|json"
    description: "What this field contains and represents"
```

### `starter_idea`
```yaml
starter_idea: "One compelling, specific idea for developers to build with this data"
```

### `build_ideas`
```yaml
build_ideas:
  - "First detailed idea with specific use case"
  - "Second idea solving a real Maharashtra problem"
  - "Third idea leveraging ML/AI capabilities"
```

### `quick_start`
```yaml
quick_start: |
  from datasets import load_dataset
  ds = load_dataset("dataset-id")
  print(ds['train'].take(3))
```

## Cost & Time

| Metric | Value |
|--------|-------|
| Total datasets | 172 |
| Tokens/dataset | 400-600 |
| Cost/dataset | ~$0.00015 |
| **Total cost** | **~$0.03** |
| **Processing time** | **30-40 min** |

## Troubleshooting

### API Key Not Found
```bash
# Check it's set
echo $ANTHROPIC_API_KEY

# Or pass explicitly
python3 scripts/complete_metadata.py --api-key "sk-ant-..."
```

### Rate Limiting Errors
The script includes automatic delays (0.2s) between API calls. If you hit rate limits:
```bash
# Increase delay in script (line 245)
time.sleep(1.0)  # Instead of 0.2
```

### YAML Parsing Errors
Some existing YAML files might have formatting issues:
```bash
# Validate all YAML files
python3 -c "
import yaml
from pathlib import Path
for f in Path('data_cards').glob('*.yaml'):
    try:
        with open(f) as file:
            yaml.safe_load(file)
    except Exception as e:
        print(f'ERROR {f.name}: {e}')
"
```

### Claude Response Not Parsing
If Claude returns malformed JSON:
```bash
# Check the .log file for response text
tail -20 .metadata_completion.log | grep "response was:"

# Dataset will be skipped and logged; resume later
```

## Next Steps

After generation completes:

1. **Review Sample** (10-20 random datasets)
   - Check ideas are specific and practical
   - Verify schema matches actual data structure
   - Ensure quick_start code is runnable

2. **Fill Manual Fields**
   - `organization`: Add official sources
   - `direct_download_url`: Add mirrors if needed
   - `citation`: Add BibTeX for papers

3. **Commit & Deploy**
   ```bash
   git add -A
   git commit -m "Complete metadata for 172 datasets

   - Generate schema definitions for all datasets
   - Add starter ideas for entrepreneurs
   - Include 3 build ideas per dataset
   - Provide quick start code snippets

   Generated with Claude Haiku API (cost: $0.03)"

   git push origin vk/15c0-complete-dataset
   ```

4. **Build & Deploy**
   ```bash
   npm run build
   npm run deploy
   ```

## Support

- **Script Issues**: Check `METADATA_COMPLETION_PLAN.md` for architecture
- **API Problems**: See Anthropic docs: https://console.anthropic.com
- **Dataset Specific**: Check CATALOG.md for source URLs
