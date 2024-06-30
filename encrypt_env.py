# /mnt/data/encrypt_env.py
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
# You must use the same key for encryption and decryption
key = Fernet.generate_key()

# Save the key to a file
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

f = Fernet(key)

# Load .env file
with open(".env", "r") as env_file:
    lines = env_file.readlines()

encrypted_lines = []
for line in lines:
    if "=" in line:
        key, value = line.split("=", 1)
        # Encrypt the value
        encrypted_value = f.encrypt(value.strip().encode()).decode()
        encrypted_lines.append(f"{key}={encrypted_value}\n")
    else:
        encrypted_lines.append(line)

# Save encrypted values in .env.encrypted file
with open(".env.encrypted", "w") as encrypted_env_file:
    encrypted_env_file.writelines(encrypted_lines)

print("Encryption completed. The .env.encrypted file has been created.")
