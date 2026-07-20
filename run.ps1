# Hand Gesture Mouse Controller - PowerShell Launcher
# This script runs the hand gesture application with proper error handling

$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

Write-Host "Starting Hand Gesture Mouse Controller..." -ForegroundColor Green
Write-Host ""
Write-Host "Controls:" -ForegroundColor Cyan
Write-Host "  - q: Quit application"
Write-Host "  - m: Toggle mirror mode"
Write-Host ""
Write-Host "Tips:" -ForegroundColor Cyan
Write-Host "  - Ensure good lighting for hand detection"
Write-Host "  - Keep your hand fully in the camera frame"
Write-Host "  - Position camera at arm's length for best results"
Write-Host ""

try {
    & .\venv\Scripts\python.exe main.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nApplication closed successfully." -ForegroundColor Green
    } else {
        Write-Host "`nApplication exited with code: $LASTEXITCODE" -ForegroundColor Red
    }
} catch {
    Write-Host "Error running application: $_" -ForegroundColor Red
}

Write-Host ""
Read-Host "Press Enter to close this window"
