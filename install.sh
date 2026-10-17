#!/usr/bin/env bash
# GovernanceOS one-click installer (read-only clone + copy into a local skills dir).
set -euo pipefail

REPO="https://github.com/zhaoxinghua09-cell/governanceos.git"
DEST="${1:-$HOME/.governanceos}"

echo "[GovernanceOS] cloning $REPO -> $DEST"
if [ -d "$DEST/.git" ]; then
  echo "[GovernanceOS] $DEST already exists; pulling latest"
  git -C "$DEST" pull --ff-only
else
  git clone --depth 1 "$REPO" "$DEST"
fi

echo "[GovernanceOS] done. Point your agent CLI at: $DEST/SKILL.md"
echo "[GovernanceOS] try: python3 $DEST/scripts/governance_flow.py --list"
