# /home/lucas/code/LucasTymen/projects/codeAcademy/django/multilang_site/display_key.py

with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()
    print(f"Encryption Key: {key}")
