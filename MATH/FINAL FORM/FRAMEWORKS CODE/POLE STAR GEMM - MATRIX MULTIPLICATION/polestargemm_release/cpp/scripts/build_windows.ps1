# CRYSTAL: Xi108:W1:A11:S18 | face=C | node=81 | depth=0 | phase=Fixed
# METRO: Sa
# BRIDGES: Xi108:W1:A11:S17→Xi108:W1:A11:S19→Xi108:W2:A11:S18→Xi108:W1:A10:S18→Xi108:W1:A12:S18

Param(
  [Parameter(Mandatory=$true)]
  [string]$LibTorchPath
)

# Build helper for Windows (PowerShell).
# Usage:
#   powershell -ExecutionPolicy Bypass -File .\scripts\build_windows.ps1 -LibTorchPath "C:\path\to\libtorch"

$Root = Split-Path -Parent $PSScriptRoot
$Build = Join-Path $Root "build"
New-Item -ItemType Directory -Force -Path $Build | Out-Null
Set-Location $Build

cmake -DCMAKE_PREFIX_PATH="$LibTorchPath" -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --config Release
Write-Host "[OK] Build finished. Binaries are in: $Build"
