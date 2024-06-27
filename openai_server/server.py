import http.server
import json
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the request handler class
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/chatbot':
            # Read the content length from the request header and the post data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data)

            # Extract the user message from the post data
            user_message = post_data.get("message")
            if user_message:
                try:
                    # Send the user message to OpenAI and get the response
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": user_message},
                        ]
                    )
                    response_text = response['choices'][0]['message']['content'].strip()
                    response_json = json.dumps({"response": response_text})

                    # Send the response back to the client
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(response_json.encode())
                except Exception as e:
                    # Handle exceptions and send an error response
                    self.send_response(500)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": str(e)}).encode())
            else:
                # Handle missing user message in the request
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "No message provided"}).encode())
        else:
            # Handle unknown paths
            self.send_response(404)
            self.end_headers()

# Function to run the server
def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8003):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
