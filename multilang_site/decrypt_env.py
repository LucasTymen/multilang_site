# decrypt_env.py

from cryptography.fernet import Fernet
import os

def decrypt_message(encrypted_message):
    encryption_key = os.getenv("ENCRYPTION_KEY")
    if not encryption_key:
        raise ValueError("No encryption key provided")
    f = Fernet(encryption_key.encode())
    decrypted_message = f.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

if __name__ == "__main__":
    import sys
    encrypted_message = sys.argv[1]
    print(decrypt_message(encrypted_message))
