#!/bin/bash
echo "Setting up Python virtual environment for Image Encryption Tool..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python from https://python.org"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing required packages..."
pip install -r requirements.txt

echo
echo "Setup complete! Virtual environment is now active."
echo "To run the tool, use: python image_encryption_tool.py input.jpg output.jpg --key 'yourkey'"