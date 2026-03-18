# CRYSTAL: Xi108:W3:A3:S29 | face=C | node=170 | depth=1 | phase=Fixed
# METRO: Sa
# BRIDGES: Xi108:W3:A3:S28→Xi108:W3:A3:S30→Xi108:W2:A3:S29→Xi108:W3:A2:S29→Xi108:W3:A4:S29

﻿param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $root
try {
    & python -m self_actualize.runtime.command_membrane @Args
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
