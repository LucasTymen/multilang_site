from cryptography.fernet import Fernet
import os

# Generate a key for encryption
key = Fernet.generate_key()
f = Fernet(key)

# Save the key in a file
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Load .env file
with open(".env", "r") as env_file:
    lines = env_file.readlines()

encrypted_lines = []
for line in lines:
    if "=" in line:
        key, value = line.split("=", 1)
        encrypted_value = f.encrypt(value.strip().encode()).decode()
        encrypted_lines.append(f"{key}=gAAAAAB{encrypted_value}\n")
    else:
        encrypted_lines.append(line)

# Save encrypted values in a new .env file
with open(".env.encrypted", "w") as encrypted_env_file:
    encrypted_env_file.writelines(encrypted_lines)

print("Encryption completed. The encryption key is saved in encryption_key.key")
