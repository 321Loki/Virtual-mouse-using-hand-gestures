@echo off
REM Test Dependencies - Hand Gesture Mouse Controller
REM This script verifies all dependencies are installed correctly

cd /d "%~dp0"
echo Testing Hand Gesture Mouse Controller Dependencies...
echo.

.\venv\Scripts\python.exe main.py --test

if %errorlevel% equ 0 (
    echo.
    echo All dependencies verified! You can now run:
    echo   - Double-click run.bat to start the application
    echo   - Or run: python main.py
    echo.
) else (
    echo.
    echo Error testing dependencies. Please check your virtual environment.
    echo.
)

pause
