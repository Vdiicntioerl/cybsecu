import os
import logging
from ciphered_gui import CipheredGUI
from cryptography.fernet import Fernet
from hashlib

class FernetGUI(CipheredGUI):
    def __init(self) -> None:
        super().__init__()
        self._key =None
    def key_derivation(self, password: str) -> bytes:
        #Salt genere aleatoirement
        salt="Bonneoumauvaisesituation".encode()
        #conversion du mot de passe en bytes
        password_bytes = password.encode()
        #password_bytes=password.encode('utf-8')
        #derivation
        kdf = Fernet(algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=480000)
        key = kdf.derive(password_bytes)
        return key
    

    def run_chat(self, sender, app_data) -> None:
        return super().run_chat(sender, app_data)
    def encrypt(self, message):
        return super().encrypt(message)
    def decrypt(self, encrypted_message):
        return super().decrypt(encrypted_message)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = FernetGUI()
    client.create()
    client.loop()    

