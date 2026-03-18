# CRYSTAL: Xi108:W1:A9:S21 | face=C | node=366 | depth=1 | phase=Cardinal
# METRO: Sa
# BRIDGES: Xi108:W1:A9:S20→Xi108:W1:A9:S22→Xi108:W2:A9:S21→Xi108:W1:A8:S21→Xi108:W1:A10:S21

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
