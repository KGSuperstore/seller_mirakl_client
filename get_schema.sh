#!/usr/bin/env bash
set -euo pipefail

# Download schemas and save as JSON in current directory.
# Overwrites existing files with the same names.

SELLER_URL="https://developer.mirakl.com/specs/content/product/mmp/rest/seller/openapi3-download.json?download"
OUT_FILE="seller-openapi3-download.json"

echo "Downloading seller schema -> ${OUT_FILE}"
curl -sSL "$SELLER_URL" -o "$OUT_FILE"

echo "Seller schema downloaded."
