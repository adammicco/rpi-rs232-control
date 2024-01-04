from serial import Serial
from time import sleep

BUS = "COM0"
BAUD = 9600

class RS232C(Serial):
    def __init__(self, bus, baud, *args, **kwargs):
        self.bus = bus
        self.baud = baud
        super().__init__(port=self.bus, baudrate=self.baud, *args, **kwargs)

    def listen(self):
        data = self.read_until(b"\b\n")
        return data

    def send_req(self, payload, await_response=False):
        self.write(bytearray(payload), 'ascii')
        if await_response:
            sleep(0.1)
            self.listen()
        pass

# if __name__ == "__main__":
#     test = RS232C(BUS, BAUD)