#!/usr/bin/env bash
set -euo pipefail

# Generate Python client from the local seller OpenAPI spec using uv.
# - Optionally refresh the spec first with ./get_schema.sh by passing --fetch
# - Overwrites existing client in place

ROOT_DIR=$(cd "$(dirname "$0")" && pwd)
cd "$ROOT_DIR"

FETCH=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --fetch)
      FETCH=true
      shift
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Usage: $0 [--fetch]" >&2
      exit 2
      ;;
  esac
done

if ! command -v uv >/dev/null 2>&1; then
  echo "Error: uv is required. Install from https://docs.astral.sh/uv/" >&2
  exit 1
fi

if [[ "$FETCH" == true ]]; then
  if [[ -x ./get_schema.sh ]]; then
    echo "Fetching latest schemas via get_schema.sh ..."
    bash ./get_schema.sh
  else
    echo "Warning: get_schema.sh not found or not executable; skipping fetch." >&2
  fi
fi

SELLER_SPEC="seller-openapi3-download.json"

if [[ ! -f "$SELLER_SPEC" ]]; then
  echo "Error: Spec file not found. Expected: $SELLER_SPEC" >&2
  echo "Hint: run: bash get_schema.sh  or  $0 --fetch" >&2
  exit 1
fi

next_version() {
  local proj_dir="$1"
  local pyproj="$proj_dir/pyproject.toml"
  [[ -f "$pyproj" ]] || { echo "0.1.0"; return; }
  python3 - "$pyproj" <<'PY'
import re, sys
from pathlib import Path
import tomllib
p = Path(sys.argv[1])
try:
    data = tomllib.loads(p.read_text())
    v = str(data.get('project', {}).get('version', 'latest-release'))
except Exception:
    v = 'latest-release'
m = re.fullmatch(r'(\d+)\.(\d+)\.(\d+)', v)
if m:
    maj, min_, pat = map(int, m.groups())
    print(f"{maj}.{min_}.{pat+1}")
else:
    # start at 0.1.0 if non-semver or missing
    print("0.1.1" if v == "0.1.0" else "0.1.0")
PY
}

set_pkg_name_and_version() {
  local proj_dir="$1"; local new_name="$2"; local new_ver="$3"
  local pyproj="$proj_dir/pyproject.toml"
  [[ -f "$pyproj" ]] || return 0
  # Rename the package (idempotent)
  sed -i '' "s/^name = \"mirakl-marketplace-ap-is-client\"/name = \"$new_name\"/" "$pyproj" || true
  # Set version inside [project]
  python3 - "$pyproj" "$new_ver" <<'PY'
import re, sys
from pathlib import Path
path = Path(sys.argv[1]); new = sys.argv[2]
text = path.read_text()
lines = text.splitlines(keepends=True)
start = None; end = len(lines)
for i, ln in enumerate(lines):
    if ln.strip() == '[project]':
        start = i; break
if start is not None:
    for j in range(start+1, len(lines)):
        if lines[j].lstrip().startswith('['):
            end = j; break
    block = ''.join(lines[start:end])
    if re.search(r'(?m)^\s*version\s*=', block):
        block_new = re.sub(r'(?m)^(\s*version\s*=\s*)\"[^\"]*\"', rf'\1"{new}"', block)
        lines[start:end] = [block_new]
    else:
        lines.insert(start+1, f'version = "{new}"\n')
    path.write_text(''.join(lines))
else:
    # fallback
    path.write_text(re.sub(r'(?m)^(\s*version\s*=\s*)\"[^\"]*\"', rf'\1"{new}"', text))
PY
}

ensure_changelog() {
  local proj_dir="$1"
  local changelog="$proj_dir/CHANGELOG.md"
  [[ -f "$changelog" ]] && return 0
  cat <<'EOF' > "$changelog"
# Changelog

This placeholder changelog enables `uv build` packaging. Update with release notes as needed.
EOF
}

# Compute next version from existing project (before overwriting)
SE_VER=$(next_version client-seller)

echo "Generating client-seller from $SELLER_SPEC ..."
uv run openapi-python-client generate \
  --path "$SELLER_SPEC" \
  --output-path client-seller \
  --overwrite \
  --meta uv || true
set_pkg_name_and_version client-seller mirakl-marketplace-seller-client "$SE_VER"
ensure_changelog client-seller

echo "Done. Client is in: client-seller/"
echo "Package name: mirakl-marketplace-seller-client ($SE_VER)"
echo "Note: If warnings appear, they stem from upstream spec quirks; most endpoints still generate."
