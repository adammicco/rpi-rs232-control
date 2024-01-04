import socketserver
from http.server import BaseHTTPRequestHandler

HOST = "localhost"
PORT = 8080

class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.request.sendall(self.data.upper())
        print(f"{self.client_address[0]}: {self.data}")

if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()