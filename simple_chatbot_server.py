import http.server
import json
import os
from urllib.parse import urlparse, parse_qs
import openai

class ChatbotHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the length of the content
        content_length = int(self.headers['Content-Length'])
        # Read the content data
        post_data = self.rfile.read(content_length)
        # Parse the JSON data
        request_data = json.loads(post_data)

        # Check if 'message' field is present in the request
        if 'message' not in request_data:
            # Send a 400 error if 'message' is not provided
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'error': 'No message field provided'}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return

        message = request_data['message']

        try:
            # Set the OpenAI API key from environment variables
            openai.api_key = os.getenv('OPENAI_API_KEY')
            # Call the OpenAI API to get a response
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": message}]
            )

            # Extract the chatbot response
            chatbot_response = response['choices'][0]['message']['content']

            # Send a 200 OK response with the chatbot's message
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'chatbot_response': chatbot_response}
            self.wfile.write(json.dumps(response).encode('utf-8'))

        except Exception as e:
            # Send a 500 error if something goes wrong
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'error': str(e)}
            self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=http.server.HTTPServer, handler_class=ChatbotHTTPRequestHandler, port=9000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
