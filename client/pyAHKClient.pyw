from ahk import AHK
from time import sleep
from socket import socket, AF_INET, SOCK_STREAM

HOST = "raspberrypi.local"
PORT = 8080

def run(data):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", 'utf-8'))
        sleep(0.1)
        # rec = str(sock.recv(1024), 'utf-8')
    pass

def send_MVLUP():
    run('MVLUP')

def send_MVLDONW():
    run('MVLDOWN')

ahk = AHK(executable_path="C:\\Program Files\\AutoHotkey\\v2\\AutoHotkey64.exe")
ahk.add_hotkey('F24', callback=send_MVLUP)
ahk.add_hotkey('F23', callback=send_MVLDONW)
ahk.start_hotkeys()
ahk.block_forever()