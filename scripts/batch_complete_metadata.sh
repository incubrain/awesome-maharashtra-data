#!/bin/bash
# Batch metadata completion with resume capability
# This script processes datasets in batches, allowing for resumption and better error handling

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_FILE="${PROJECT_DIR}/.metadata_completion.log"
CHECKPOINT_FILE="${PROJECT_DIR}/.metadata_checkpoint"

# Configuration
BATCH_SIZE=10
DATASETS_TOTAL=172

# Read checkpoint if it exists
START_FROM=0
if [ -f "$CHECKPOINT_FILE" ]; then
    START_FROM=$(cat "$CHECKPOINT_FILE")
    echo "Resuming from dataset #$START_FROM"
fi

# Check API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: ANTHROPIC_API_KEY environment variable not set"
    exit 1
fi

echo "Starting metadata completion for $DATASETS_TOTAL datasets"
echo "Batch size: $BATCH_SIZE"
echo "Start from: $START_FROM"
echo ""

# Process in batches
for ((i = START_FROM; i < DATASETS_TOTAL; i += BATCH_SIZE)); do
    END=$((i + BATCH_SIZE))
    if [ $END -gt $DATASETS_TOTAL ]; then
        END=$DATASETS_TOTAL
    fi

    echo "[$i/$DATASETS_TOTAL] Processing batch: $i to $END"

    # Run batch
    python3 "$SCRIPT_DIR/complete_metadata.py" --start-from "$i" 2>&1 | tee -a "$LOG_FILE"

    # Save checkpoint
    echo $((i + BATCH_SIZE)) > "$CHECKPOINT_FILE"

    # Sleep between batches to avoid rate limiting
    sleep 2
done

# Cleanup checkpoint
rm -f "$CHECKPOINT_FILE"

echo ""
echo "✓ Metadata completion finished!"
echo "Log saved to: $LOG_FILE"
