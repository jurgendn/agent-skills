#!/usr/bin/env bash
set -euo pipefail

REPO="https://github.com/jurgendn/agent-skills.git"
SKILL="*"
usage() {
  cat <<'EOF'
Usage: ./scripts/install.sh [--repo URL] [--skill NAME_OR_GLOB]

Install skills from this repository using the official skills CLI.

Options:
  --repo URL             Repository URL to install from
  --skill NAME_OR_GLOB   Skill name or glob to install (default: *)
  -h, --help             Show this help

Examples:
  ./scripts/install.sh
  ./scripts/install.sh --skill ielts-writing-task2
  ./scripts/install.sh --repo https://github.com/jurgendn/agent-skills.git
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --repo)
      REPO="${2:?Missing repo URL}"
      shift 2
      ;;
    --skill)
      SKILL="${2:?Missing skill name or glob}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown option: %s\n' "$1" >&2
      usage
      exit 1
      ;;
  esac
done

if ! command -v npx >/dev/null 2>&1; then
  printf 'Error: npx not found. Install Node.js first.\n' >&2
  exit 1
fi

cmd=(npx skills add "$REPO" --skill "$SKILL")

printf 'Running:'
printf ' %q' "${cmd[@]}"
printf '\n'

"${cmd[@]}"
