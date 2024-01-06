import serial
import glob
from time import sleep

BUS = glob.glob("/dev/ttyUSB*")[0]
BAUD = 9600

class RS232C(serial.Serial):
    def __init__(self, bus, baud, *args, **kwargs):
        self.bus = bus
        self.baud = baud
        super().__init__(port=self.bus, baudrate=self.baud, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1, *args, **kwargs)

    # TODO get reading from the RS-232C port working. Need to validate that anything is actually being sent
    # def listen(self):
    #     data = self.read_until(bytearray("\r\n", 'ascii'))
    #     self.read()
    #     return data

    def send_req(self, cmd, await_response=False, start_seq='!1', end_seq='\r\n'):
        self.write(bytearray(f"{start_seq}{cmd}{end_seq}", 'ascii'))
        # if await_response:
        #     sleep(0.1)
        #     self.listen()
        pass