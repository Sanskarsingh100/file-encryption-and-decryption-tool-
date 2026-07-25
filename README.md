# file-encryption-and-decryption-tool-
file-encrption-and-decription-tool
File Encryption & Decryption Tool 🔒
A simple Python application for encrypting and decrypting files locally using symmetric key encryption (Fernet / AES).

⚠️ Warning: This script performs in-place file modification. Encrypting or decrypting a file overwrites its content directly. Always keep a backup copy of your important files before processing them.

🚀 Features
Key Generation: Generates a secure, random encryption key and saves it to secret.key.
File Encryption: Encrypts any file using the generated secret.key.
File Decryption: Decrypts an encrypted file back to its original state[cite: 1].
CLI Interface: Easy-to-use menu system in the terminal[cite: 1].
📋 Prerequisites
Python 3.x
cryptography library[cite: 1]
To install the required dependency, run:

pip install cryptography




📂 Project Structure
Plaintext
├── app.py          # Main application script
├── secret.key      # Encryption key (generated upon first run)
└── README.md       # Project documentation




🛠️ How to Run
Clone the repository:

Bash
git clone [https://github.com/your-username/file-encryption-and-decryption-tool.git](https://github.com/your-username/file-encryption-and-decryption-tool.git)
cd file-encryption-and-decryption-tool
Run the application:

Bash
python app.py
Follow the interactive menu:

Plaintext
--- File Encryptor & Decryptor ---
1. Generate Key
2. Encrypt File
3. Decrypt File




📖 Usage Guide
Option 1 (Generate Key):

Run this first before encrypting or decrypting any files[cite: 1].

It creates a secret.key or and other named file in your root folder[cite: 1].

Option 2 (Encrypt File):

Enter the name or path of the target file (e.g., document.txt or photos/image.png).

The file contents will be converted to encrypted ciphertext[cite: 1].

Option 3 (Decrypt File):

Enter the name or path of the encrypted file.

Using secret.key, the file will be restored to its original plaintext format[cite: 1].



