@echo off
echo Setting up Python virtual environment for Image Encryption Tool...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Setup complete! Virtual environment is now active.
echo To run the tool, use: python image_cipher.py input.jpg output.jpg --key "yourkey"
echo.
pause