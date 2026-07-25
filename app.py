import os
from cryptography.fernet import Fernet

def generate_key():
    """Generates and saves a secret encryption key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print(" [✓] Secret key generated and saved as 'secret.key'.")

def load_key():
    """Loads the secret key from the current directory."""
    if not os.path.exists("secret.key"):
        raise FileNotFoundError("Key file 'secret.key' not found! Generate it first.")
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    """Encrypts a file given its filename."""
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)
    
    print(f" [✓] '{filename}' encrypted successfully!")

def decrypt_file(filename):
    """Decrypts an encrypted file back to its original state."""
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    print(f" [✓] '{filename}' decrypted successfully!")

if __name__ == "__main__":
    print("\n--- File Encryptor & Decryptor ---")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    
    choice = input("\nChoose an option (1-3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        target_file = input("Enter the path/name of the file to encrypt: ")
        encrypt_file(target_file)
    elif choice == "3":
        target_file = input("Enter the path/name of the file to decrypt: ")
        decrypt_file(target_file)
    else:
        print("Invalid choice!")