from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Cyber Deck Web Server Settings
HOST = "0.0.0.0"
PORT = 8000

# Make the server run from the folder containing this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CyberDeckHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Open index.html when visiting the server
        if self.path == "/":
            self.path = "/index.html"

        return super().do_GET()


# Start Cyber Deck server
server = HTTPServer((HOST, PORT), CyberDeckHandler)

print("================================")
print("        CYBER DECK ONLINE")
print("================================")
print(f"Server running on port: {PORT}")
print("Open in browser:")
print("http://RASPBERRY_PI_IP:8000")
print("================================")

try:
    server.serve_forever()

except KeyboardInterrupt:
    print("\nCyber Deck shutting down...")
    server.server_close()