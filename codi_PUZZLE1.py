import time
import board
import busio
from adafruit_pn532.i2c import PN532_I2C
from digitalio import DigitalInOut

class NFCReader:
    def __init__(self, debug=False):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.pn532 = PN532_I2C(self.i2c, debug=debug)
        self.pn532.SAM_configuration()
        print("Esperant una targeta NFC...")

    def read_uid(self):
        uid = None
        while uid is None:
            uid = self.pn532.read_passive_target(timeout=0.5)

        uid_hex = ''.join([f'{i:02X}' for i in uid])
        print("Targeta detectada!")
        print(f"UID de la targeta: {uid_hex}")
        
        time.sleep(1)  
        return uid_hex

if __name__ == "__main__":
    lector = NFCReader(debug=True)
    lector.read_uid()
