# /home/lucas/code/LucasTymen/projects/codeAcademy/django/multilang_site/decrypt_env.py

from cryptography.fernet import Fernet
import os

# Load the encryption key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

f = Fernet(key)

# Load encrypted .env file
with open(".env.encrypted", "r") as encrypted_env_file:
    lines = encrypted_env_file.readlines()

decrypted_lines = []
for line in lines:
    if "=" in line:
        key, encrypted_value = line.split("=", 1)
        try:
            # Decrypt the encrypted value
            decrypted_value = f.decrypt(encrypted_value.strip().encode()).decode()
            decrypted_lines.append(f"{key}={decrypted_value}\n")
        except Exception as e:
            print(f"Error decrypting {key}: {e}")
            decrypted_lines.append(f"{key}={encrypted_value.strip()}\n")  # Keep the encrypted value if decryption fails
    else:
        decrypted_lines.append(line)

# Save decrypted values in .env file
with open(".env", "w") as decrypted_env_file:
    decrypted_env_file.writelines(decrypted_lines)

print("Decryption completed. The .env file has been created.")
