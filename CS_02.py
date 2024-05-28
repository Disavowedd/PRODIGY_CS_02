from PIL import Image

def encrypt(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            if y % 2 == 0:
                new_x = (x - 62) % width  
            else:
                new_x = x  
            new_y = y
            encrypted_img.putpixel((new_x, new_y), img.getpixel((x, y)))

    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            if y % 2 == 0:
                new_x = (x + 62) % width  
            else:
                new_x = x  
            new_y = y
            decrypted_img.putpixel((new_x, new_y), img.getpixel((x, y)))

    decrypted_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Welcome to the Image Encryption Tool")
    choice = input("Would you like to encrypt or decrypt an image? (1 for encrypt, 2 for decrypt): ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter '1' for encrypt or '2' for decrypt.")
        return
    
    if choice == "1":
        print("Encrypting...")
    else:
        print("Decrypting...")

    image_path = input("Enter the path to the image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()

    if choice == '1':
        encrypt(image_path, output_path)
    else:
        decrypt(image_path, output_path)

if __name__ == "__main__":
    main()
