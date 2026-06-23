#!/usr/bin/env bash
# Compile a Beamer deck to PDF, reproducibly and with no manual steps.
#
# The deck-beamer-* skills promise a .tex that compiles "with no manual edits
# beyond dropping in figure files". This script is that compile step, so the
# exact invocation (latexmk flags, two-pass fallback, notes handling) is not
# re-guessed each time.
#
# Usage:
#   ./compile.sh [file.tex]        # compile (defaults to the only/ﬁrst *.tex here)
#   ./compile.sh -c [file.tex]     # compile, then remove aux files
#   ENGINE=lualatex ./compile.sh   # override engine (default: pdflatex)
#
# Needs a LaTeX install (TeX Live / MacTeX). metropolis + pgfplots are assumed
# by the bundled preamble; install them if compilation reports them missing.
set -euo pipefail

CLEAN=0
if [[ "${1:-}" == "-c" ]]; then CLEAN=1; shift; fi

TEX="${1:-}"
if [[ -z "$TEX" ]]; then
  mapfile -t found < <(ls -1 ./*.tex 2>/dev/null || true)
  if [[ ${#found[@]} -eq 0 ]]; then
    echo "error: no .tex file given and none found in $(pwd)" >&2; exit 1
  elif [[ ${#found[@]} -gt 1 ]]; then
    echo "error: multiple .tex files here — pass one explicitly:" >&2
    printf '  %s\n' "${found[@]}" >&2; exit 1
  fi
  TEX="${found[0]}"
fi
[[ -f "$TEX" ]] || { echo "error: no such file: $TEX" >&2; exit 1; }

ENGINE="${ENGINE:-pdflatex}"
base="$(basename "${TEX%.tex}")"
echo ">> compiling $TEX with $ENGINE"

if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -"$ENGINE" -interaction=nonstopmode -halt-on-error "$TEX"
  [[ $CLEAN -eq 1 ]] && latexmk -c "$TEX"
else
  # Two passes resolve \tableofcontents, overlays, and cross-references.
  echo ">> latexmk not found; running $ENGINE twice"
  "$ENGINE" -interaction=nonstopmode -halt-on-error "$TEX"
  "$ENGINE" -interaction=nonstopmode -halt-on-error "$TEX"
  if [[ $CLEAN -eq 1 ]]; then
    rm -f "$base".{aux,log,nav,out,snm,toc,vrb}
  fi
fi

echo ">> done: ${base}.pdf"
