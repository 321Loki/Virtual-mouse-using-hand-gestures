@echo off
REM Hand Gesture Mouse Controller Launcher
REM This script runs the hand gesture application

cd /d "%~dp0"
echo Starting Hand Gesture Mouse Controller...
echo.
echo Make sure:
echo   - Your webcam is connected
echo   - No other app is using the camera
echo   - You have good lighting
echo.
echo Controls:
echo   - q: Quit
echo   - m: Toggle mirror mode
echo.
timeout /t 3

.\venv\Scripts\python.exe main.py

if %errorlevel% neq 0 (
    echo.
    echo Error occurred. Press any key to exit...
    pause
)
