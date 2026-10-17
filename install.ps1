# GovernanceOS one-click installer (Windows PowerShell).
$ErrorActionPreference = "Stop"

$Repo = "https://github.com/zhaoxinghua09-cell/governanceos.git"
$Dest = if ($args.Count -ge 1) { $args[0] } else { Join-Path $HOME ".governanceos" }

Write-Host "[GovernanceOS] cloning $Repo -> $Dest"
if (Test-Path (Join-Path $Dest ".git")) {
    Write-Host "[GovernanceOS] $Dest already exists; pulling latest"
    git -C $Dest pull --ff-only
} else {
    git clone --depth 1 $Repo $Dest
}

Write-Host "[GovernanceOS] done. Point your agent CLI at: $Dest\SKILL.md"
Write-Host "[GovernanceOS] try: python3 $Dest\scripts\governance_flow.py --list"
