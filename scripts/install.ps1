param(
    [string]$Repo = "https://github.com/jurgendn/agent-skills.git",
    [string]$Skill = "*",
    [switch]$NoFullDepth
)

$npx = Get-Command npx -ErrorAction SilentlyContinue

if (-not $npx) {
    Write-Error "npx not found. Install Node.js first."
    exit 1
}

$argsList = @("skills", "add", $Repo, "--skill", $Skill)

if (-not $NoFullDepth) {
    $argsList += "--full-depth"
}

Write-Host "Running: npx $($argsList -join ' ')"

& npx @argsList

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
