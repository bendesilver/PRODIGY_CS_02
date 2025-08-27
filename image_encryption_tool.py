from PIL import Image
import argparse
import sys

def check_dependencies():
    """Check if required packages are installed"""
    try:
        from PIL import Image
        return True
    except ImportError:
        print("Error: Pillow library is not installed.")
        print("Please install it using: pip install pillow")
        print("Or run the setup script for your OS:")
        print("  Windows: run setup_env.bat")
        print("  Mac/Linux: run setup_env.sh")
        return False

def process_image(input_path, output_path, key):
    # Check if Pillow is available
    if not check_dependencies():
        sys.exit(1)
    
    try:
        # Open the image
        img = Image.open(input_path)
        pixels = img.load()
        
        # Convert key to integer seed (0-255)
        seed = sum(ord(c) for c in key) % 256
        
        # Get image dimensions
        width, height = img.size
        
        # Process each pixel
        for i in range(width):
            for j in range(height):
                if img.mode == 'RGB':
                    r, g, b = pixels[i, j]
                    pixels[i, j] = (r ^ seed, g ^ seed, b ^ seed)
                elif img.mode == 'RGBA':
                    r, g, b, a = pixels[i, j]
                    pixels[i, j] = (r ^ seed, g ^ seed, b ^ seed, a)
                elif img.mode == 'L':
                    pixels[i, j] = pixels[i, j] ^ seed
        
        # Save the processed image
        img.save(output_path)
        print(f"Image processed successfully and saved to {output_path}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
    except Exception as e:
        print(f"Error processing image: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Image Encryption/Decryption Tool using XOR Cipher')
    parser.add_argument('input', help='Path to input image file')
    parser.add_argument('output', help='Path to save processed image')
    parser.add_argument('--key', required=True, help='Encryption/Decryption key (string)')
    
    args = parser.parse_args()
    
    process_image(args.input, args.output, args.key)

if __name__ == '__main__':
    main()
