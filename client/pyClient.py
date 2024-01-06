import socket
import sys
import argparse

HOST = "raspberrypi.local"
PORT = 8080

parser = argparse.ArgumentParser()
parser.add_argument('data', type=str)
args = parser.parse_args()
data = args.data.upper()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", 'utf-8'))
    # rec = str(sock.recv(1024), 'utf-8')

# print(f"Sent: {data}")
# print(f"Recieved: {rec}")