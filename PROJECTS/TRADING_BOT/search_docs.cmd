# CRYSTAL: Xi108:W1:A1:S24 | face=S | node=352 | depth=3 | phase=Mutable
# METRO: Sa
# BRIDGES: Xi108:W1:A1:S23→Xi108:W1:A1:S25→Xi108:W2:A1:S24→Xi108:W1:A2:S24

@echo off
setlocal
set SCRIPT_DIR=%~dp0
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%search_docs.ps1" %*
set EXIT_CODE=%ERRORLEVEL%
endlocal & exit /b %EXIT_CODE%
