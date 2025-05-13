from PIL import Image
import argparse

def process_image(input_path, output_path, key):
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

def main():
    parser = argparse.ArgumentParser(description='Image Encryption/Decryption Tool using XOR Cipher')
    parser.add_argument('input', help='Path to input image file')
    parser.add_argument('output', help='Path to save processed image')
    parser.add_argument('--key', required=True, help='Encryption/Decryption key (string)')
    
    args = parser.parse_args()
    
    try:
        process_image(args.input, args.output, args.key)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()