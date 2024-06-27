# openai_server/Dockerfile
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8003 available to the world outside this container
EXPOSE 8003

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]
