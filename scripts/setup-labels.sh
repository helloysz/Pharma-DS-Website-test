#!/usr/bin/env bash
#
# Create/update the PharmaDS website-workflow labels defined in .github/labels.yml.
# Idempotent: safe to run repeatedly (uses `gh label create --force` to upsert).
#
# Requirements: GitHub CLI (`gh`) authenticated with access to the repo.
# Usage:
#   bash scripts/setup-labels.sh                 # uses current repo (from git remote)
#   REPO=helloysz/Pharma-DS-Website-test bash scripts/setup-labels.sh
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABELS_FILE="${SCRIPT_DIR}/../.github/labels.yml"
REPO_ARG=()
if [[ -n "${REPO:-}" ]]; then
  REPO_ARG=(--repo "${REPO}")
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "error: GitHub CLI (gh) is not installed. See https://cli.github.com/" >&2
  exit 1
fi
if [[ ! -f "${LABELS_FILE}" ]]; then
  echo "error: labels file not found at ${LABELS_FILE}" >&2
  exit 1
fi

# Parse the simple `- name/color/description` YAML into TAB-separated records.
parse() {
  awk '
    /^[[:space:]]*-[[:space:]]*name:/ {
      if (have) { print name "\t" color "\t" desc }
      name=parse_val($0); color=""; desc=""; have=1; next
    }
    /^[[:space:]]*color:/       { color=parse_val($0); next }
    /^[[:space:]]*description:/ { desc=parse_val($0); next }
    END { if (have) print name "\t" color "\t" desc }
    function parse_val(line,   v) {
      sub(/^[^:]*:[[:space:]]*/, "", line)
      v=line
      gsub(/^"|"$/, "", v)
      return v
    }
  ' "${LABELS_FILE}"
}

count=0
while IFS=$'\t' read -r name color desc; do
  [[ -z "${name}" ]] && continue
  echo "→ ${name}"
  gh label create "${name}" --color "${color}" --description "${desc}" --force "${REPO_ARG[@]}"
  count=$((count + 1))
done < <(parse)

echo "Done. Upserted ${count} labels."
