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

def send_PWR01():
    run('PWR01')
    sleep(0.5)
    run('SLI10')

def send_PWR00():
    run('PWR00')

def send_mutePause():
    run('NTCP/P')
    sleep(0.5)
    run('AMTTG')

ahk = AHK(executable_path="C:\\Program Files\\AutoHotkey\\v2\\AutoHotkey64.exe")
ahk.add_hotkey('F19', callback=send_MVLUP)
ahk.add_hotkey('F18', callback=send_MVLDONW)
ahk.add_hotkey('F17', callback=send_PWR01)
ahk.add_hotkey('F16', callback=send_PWR00)
ahk.add_hotkey('F15', callback=send_mutePause)
ahk.start_hotkeys()
ahk.block_forever()