
from fernet_gui import FernetGUI
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import time
import base64
import logging

#Duree de vie d'un message en sec
TTL = 30-45

class TimeFernetGUI(FernetGUI):
    def encrypt(self, message):
        f=Fernet(self._key)
        temps = int(time.time())
        encrypted_message=f.encrypt_at_time(bytes(message,'utf-8'),current_time=temps)
        return encrypted_message

    def decrypt(self, encrypted_message):
        message = base64.b64decode(encrypted_message['data'])
        temps = int(time.time())
        f = Fernet(self._key)
        try:
            return f.decrypt_at_time(message,ttl=TTL,current_time= temps).decode()
        except InvalidToken as e:
            raise logging.exception("Invalid Token")
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = TimeFernetGUI()
    client.create()
    client.loop()    


