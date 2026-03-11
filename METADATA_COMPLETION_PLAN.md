# Metadata Completion Plan for 248+ Datasets

## Overview

This epic tracks the completion of metadata for all 248+ datasets in the Awesome Marathi Datasets catalog. The goal is to make the catalog truly actionable by filling in missing fields that enable developers and entrepreneurs to immediately use the data.

## Audit Summary (2026-03-11)

- **172 datasets** listed in CATALOG.md
- **21 YAML data cards** created (out of 172 needed)
- **0/248** datasets have complete advanced metadata

### Metadata Gaps by Field

| Field | Status | Count | Priority |
|-------|--------|-------|----------|
| `schema` | Missing | 248/248 | 🔴 Critical |
| `starter_idea` | Missing | 248/248 | 🔴 Critical |
| `build_ideas` | Missing | 248/248 | 🔴 Critical |
| `quick_start` | Partially | 10/248 | 🟡 High |
| `organization` | Partial | 88/248 | 🟡 High |
| `direct_download_url` | Missing | ~150/248 | 🟡 High |
| `citation` | Missing | ~200/248 | 🟠 Medium |

## Solution Architecture

### 1. Intelligent Metadata Generation Script (`scripts/complete_metadata.py`)

**What it does:**
- Parses CATALOG.md to extract all 172+ datasets
- Creates YAML data cards for datasets missing them
- Uses Claude Haiku API to intelligently generate:
  - `schema`: Field definitions (name, type, description)
  - `starter_idea`: One compelling idea for entrepreneurs
  - `build_ideas`: 2-3 specific, detailed implementation ideas
  - `quick_start`: Runnable Python code snippets

**Why Haiku:**
- Cost-effective for batch processing (estimates: ~$2-5 for all 248 datasets)
- Fast enough for non-blocking processing
- Sufficient quality for guided metadata generation

**Key Features:**
- Resume capability (checkpoint system)
- Batch processing with rate limiting
- Dry-run mode for preview
- Filtering by dataset slug
- Error handling and logging

### 2. Execution Strategy

#### Phase 1: Setup (✓ Completed)
- [x] Create `complete_metadata.py` script
- [x] Create `batch_complete_metadata.sh` wrapper
- [x] Test parsing and dry-run mode
- [x] Verify API integration

#### Phase 2: Initial Generation (Ready to Execute)

**Command to run all datasets:**
```bash
export ANTHROPIC_API_KEY="your-key-here"
python3 scripts/complete_metadata.py
```

**For batch processing:**
```bash
bash scripts/batch_complete_metadata.sh
```

**For testing before full run:**
```bash
python3 scripts/complete_metadata.py --limit 10  # Test first 10
```

#### Phase 3: Verification & Refinement
- Review generated metadata for quality
- Manually fix any AI hallucinations
- Fill in missing organization/URLs manually if needed
- Run citation extraction for academic datasets

#### Phase 4: Integration
- Commit all data cards to git
- Update README.md badges (248 complete ✓)
- Build/deploy updated catalog website
- Announce availability to community

## File Structure

```
awesome-marathi-datasets/
├── CATALOG.md                              # Master list (172 datasets)
├── data_cards/
│   ├── _template.yaml                      # Template for new cards
│   ├── l3cube-mahacorpus.yaml             # (20 existing)
│   └── [148 more to create]                # New cards to be generated
├── scripts/
│   ├── complete_metadata.py               # Main generation script ✓
│   ├── batch_complete_metadata.sh         # Batch wrapper ✓
│   └── filter_datagov.py                  # Existing helper
├── METADATA_COMPLETION_PLAN.md            # This file
└── .metadata_checkpoint                   # (auto-created during batch runs)
```

## Prompt Engineering Details

### Claude Haiku Prompt Structure

The script uses a carefully engineered prompt that:

1. **Provides context:**
   - Dataset title, category, modality
   - License, primary use case
   - Existing description/metadata if available

2. **Requests JSON output:**
   - Ensures parseable response
   - Specifies exact field names
   - Includes format examples

3. **Enforces constraints:**
   - Schema: 3-5 key fields relevant to modality
   - Starter idea: Single compelling sentence
   - Build ideas: 3 specific, actionable items
   - Quick start: Runnable code (3-4 lines)

4. **Context optimization:**
   - Emphasizes Marathi/Maharashtra relevance
   - Mentions real business problems
   - Encourages practical, implementable ideas

### Example Generated Metadata

For `ai4bharat-samanantar-mr` (English-Marathi parallel corpus):

```yaml
schema:
  - field: "english_text"
    type: "string"
    description: "English sentence from source parallel corpus"
  - field: "marathi_text"
    type: "string"
    description: "Marathi translation of the English sentence"
  - field: "domain"
    type: "string"
    description: "Source domain (news, wiki, books, etc.)"
  - field: "confidence"
    type: "float"
    description: "Alignment confidence score (0-1)"

starter_idea: "Build a Marathi sentence translator API for mobile apps using this parallel corpus to fine-tune a small model."

build_ideas:
  - "Create a Marathi↔English terminology dictionary extractor with UI for SME validation"
  - "Build a low-latency machine translation service for Government websites and agri apps"
  - "Fine-tune an open LLM on this data and deploy as a HF Space for accessibility"

quick_start: |
  from datasets import load_dataset
  ds = load_dataset("ai4bharat/samanantar")
  for example in ds['train'].take(3):
      print(f"EN: {example['english_text']}")
      print(f"MR: {example['marathi_text']}\n")
```

## Cost Estimation

### API Costs

- **Input tokens:** ~100-200 per dataset (description context)
- **Output tokens:** ~300-400 per dataset (schema + ideas + code)
- **Total per dataset:** ~400-600 tokens
- **Price (Haiku):** $0.08 per 1M input, $0.24 per 1M output
- **Cost per dataset:** ~$0.00015
- **Total for 172 datasets:** ~$0.03
- **Safety margin (2x):** ~$0.06

**Alternative:** Batch all 172 in one clever request = even lower cost.

### Time Estimation

- **Per dataset:** 0.5-1s (API call + parsing + save)
- **172 datasets:** ~2-3 minutes serial
- **With rate limiting (0.2s sleep):** ~35-40 minutes
- **In batches of 10:** Multiple batches, ~5-10 minute overhead

## Manual Follow-up Tasks

After script completes, these items may need manual attention:

### 1. Organization/Author Field
- Search GitHub/academic sources for missing organizations
- Add official sources for government datasets
- Link researchers to dataset provenance

### 2. Direct Download URLs
- Extract from dataset homepages
- Handle redirects and mirror links
- Mark if download requires registration

### 3. Citation Information
- Extract BibTeX from academic papers
- Link to DOI/arXiv when available
- Add dataset-specific citations

### 4. Quality Review
- Sample review of generated metadata (10%)
- Check for hallucinated links/information
- Verify schema matches actual data format

## Success Criteria

- ✓ 100% of 172 datasets have YAML files in `data_cards/`
- ✓ 100% have populated `schema` field
- ✓ 100% have populated `starter_idea`
- ✓ 100% have populated `build_ideas` (3+ ideas)
- ✓ 100% have populated `quick_start` snippets
- ✓ 90%+ have `organization` field
- ✓ 85%+ have `direct_download_url`
- ✓ 80%+ have `citation` information
- ✓ Manual review passes quality check

## Related Issues/Tasks

- Create web interface for browsing/filtering datasets by startup idea
- Build dataset similarity engine for recommendations
- Set up automated link checking for URLs
- Create community data card contribution process
- Extract dataset schemas automatically from sample data

## Resources

- **Catalog Master:** `CATALOG.md` (172 entries, 31KB)
- **YAML Template:** `data_cards/_template.yaml`
- **Scripts:** `scripts/complete_metadata.py`, `batch_complete_metadata.sh`
- **Documentation:** This file, README.md

## Questions & Troubleshooting

### Q: Why not use a larger model like Opus?
A: Haiku is 2-3x cheaper ($0.08-$0.24 vs $0.30-$0.90 per M tokens) and fast enough for this task. Reserve Opus for quality review/refinement if needed.

### Q: Can I resume if the script crashes?
A: Yes! The script supports `--start-from N` flag and batch script auto-saves checkpoints.

### Q: How do I know the generated ideas are good?
A: Manual review of 10-20 samples is recommended. Look for:
- Specific, not generic ideas
- Maharashtra/Marathi relevance
- Feasible with available tools
- Actual real-world value

### Q: What about non-Marathi datasets?
A: Script handles any dataset but prompt emphasizes Marathi context. Datasets marked `maharashtra_specific: false` may need more adjustment.

### Q: Can I add custom prompts for specific dataset categories?
A: Yes! Modify `generate_metadata_with_claude()` to branch on `category` field and use specialized prompts for each domain.
