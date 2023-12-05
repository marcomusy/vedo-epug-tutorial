#!/bin/bash
# source run_all.sh
#
for f in *.py; do
    echo "Processing: $f"
    python "$f"
done