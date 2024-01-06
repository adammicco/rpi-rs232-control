import glob
import socketserver
from rs232com import RS232C

HOST = "raspberrypi.local"
PORT = 8080

BUS = glob.glob("/dev/ttyUSB*")[0]
BAUD = 9600
rs232 = RS232C(bus=BUS, baud=BAUD)

class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.request.sendall(self.data.upper())
        print(f"{self.client_address[0]}: {self.data.decode('utf-8')}")
        rs232.send_req(self.data.decode('utf-8'))

if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()