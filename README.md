# Image Encryption Tool

A Python-based image encryption tool that uses XOR pixel manipulation for basic image encryption/decryption.

## Features
- XOR-based pixel encryption
- Support for RGB, RGBA, and grayscale images
- Command-line interface
- Virtual environment setup scripts
- Cross-platform compatibility

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bendesilver/PRODIGY_CS_02.git
cd image_encryption_tool

  USAGE

 Encrypt an image
python src/image_encrytpion.py input.jpg encrypted.png --key "mysecretkey"

 Decrypt an image
python src/image_encryption_tool.py encrypted.png decrypted.png --key "mysecretkey"


Technologies Used
Python 3.x

Pillow (PIL Fork) library

XOR cipher algorithm
