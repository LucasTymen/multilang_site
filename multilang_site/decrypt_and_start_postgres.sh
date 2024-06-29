#!/bin/bash

# Load environment variables
source /code/.env

# Decrypt the passwords
export POSTGRES_PASSWORD=$(python -c "from decrypt_env import decrypt_message; print(decrypt_message('$ENCRYPTED_DB_PASSWORD'))")
export DB_PASSWORD=$POSTGRES_PASSWORD
export SECRET_KEY=$(python -c "from decrypt_env import decrypt_message; print(decrypt_message('$ENCRYPTED_SECRET_KEY'))")
export OPENAI_API_KEY=$(python -c "from decrypt_env import decrypt_message; print(decrypt_message('$ENCRYPTED_OPENAI_API_KEY'))")

# Start the PostgreSQL server
exec postgres -D /var/lib/postgresql/data

# Decrypt the PostgreSQL password and save it to a variable
ENCRYPTED_DB_PASSWORD=$(printenv ENCRYPTED_DB_PASSWORD)
DB_PASSWORD=$(python -c "from decrypt_env import decrypt_message; print(decrypt_message('${ENCRYPTED_DB_PASSWORD}'))")

# Set the decrypted password as an environment variable
export POSTGRES_PASSWORD=$(python /code/decrypt_env.py ${ENCRYPTED_DB_PASSWORD})

# Start the PostgreSQL server
docker-entrypoint.sh postgres
