# CRYSTAL: Xi108:W1:A12:S29 | face=S | node=435 | depth=3 | phase=Mutable
# METRO: Sa
# BRIDGES: Xi108:W1:A12:S28→Xi108:W1:A12:S30→Xi108:W2:A12:S29→Xi108:W1:A11:S29

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
