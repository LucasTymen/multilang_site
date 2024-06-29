# generate_and_encrypt.py
from cryptography.fernet import Fernet
import os

# Générer une clé de chiffrement
key = Fernet.generate_key()
cipher = Fernet(key)

# Afficher la clé pour que vous puissiez l'ajouter à votre .env
print("Encryption Key:", key.decode())

# Valeurs à chiffrer
data = {
    "DB_PASSWORD": "123password123",
    "OPENAI_API_KEY": "sk-proj-Lf2PQVAMNGBIK8TUSi1ET3BlbkFJ14iMamlXzcGfcS1LzJFb",
    "SECRET_KEY": 'aze"é&AZE321'
}

# Chiffrer les valeurs
encrypted_data = {k: cipher.encrypt(v.encode()).decode() for k, v in data.items()}

# Afficher les valeurs chiffrées pour les ajouter à votre .env
for key, value in encrypted_data.items():
    print(f"ENCRYPTED_{key}={value}")
