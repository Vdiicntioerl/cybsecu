import os
import logging

import dearpygui.dearpygui as dpg
from basic_gui import BasicGUI
from chat_client import ChatClient
from generic_callback import GenericCallback

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend

import base64

# default values used to populate connection window
DEFAULT_VALUES = {
    "host" : "127.0.0.1",
    "port" : "6666",
    "name" : "foo",
    "password" : ""
}

class CipheredGUI(BasicGUI):
    def __init__(self) -> None:
        super().__init__()
        self._key = None

    def _create_connection_window(self) -> None:
       with dpg.window(label="Connection", pos=(200, 150), width=400, height=300, show=False, tag="connection_windows"):           
        for field in ["host", "port", "name"]:
            with dpg.group(horizontal=True):
                dpg.add_text(field)
                dpg.add_input_text(default_value=DEFAULT_VALUES[field], tag=f"connection_{field}")
        with dpg.group(horizontal=True):
            dpg.add_text("password")
            dpg.add_input_text(default_value="",tag=f"connection_password", password=True)
        dpg.add_button(label="Connect", callback=self.run_chat)
        
    def key_derivation(self,password:str)-> bytes:
            #Salt genere aleatoirement
            salt="Bonneoumauvaisesituation".encode()
            #conversion du mot de passe en bytes
            password_bytes = password.encode()
            #password_bytes=password.encode('utf-8')
            #derivation
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                            length=32,
                            salt=salt,
                            iterations=480000)
            key = kdf.derive(password_bytes)
            return key 

    def run_chat(self, sender, app_data)->None:
        # callback used by the connection windows to start a chat session
        host = dpg.get_value("connection_host")
        port = int(dpg.get_value("connection_port"))
        name = dpg.get_value("connection_name")
        password = dpg.get_value("connection_password")
        self._log.info(f"Connecting {name}@{host}:{port}")

        self._callback = GenericCallback()

        self._client = ChatClient(host, port)
        self._client.start(self._callback)
        self._client.register(name)

        dpg.hide_item("connection_windows")
        dpg.show_item("chat_windows")
        dpg.set_value("screen", "Connecting")

        #appel de la fonction de derivation de cle
        self._key = self.key_derivation(password)

       
    
    def encrypt(self, message):
        # Generation d'un vecteur d'iniitalisation aleatoire
        iv=os.urandom(16)

        #Creation d'un objet Cipher en utilisant l'algorithme AES
        cipher = Cipher(algorithms.AES(self._key), 
                        modes.CTR(iv),
                        backend=default_backend()
                        )
        #Generation du message
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()
        encrypted_message = encryptor.update(padded_data) + encryptor.finalize()


        return (encrypted_message , iv)
    
    def decrypt(self, encrypted_message):
        #Recuperation de l'iv puis du message chiffre en base 64
        iv = base64.b64decode(encrypted_message[1]['data'])
        encrypted_messag = base64.b64decode(encrypted_message[0]['data'])

        #Fonction dechiffrage
        cipher= Cipher(
            algorithms.AES(self._key),
            modes.CTR(iv),
            backend=default_backend()
        )

        #Dechiffrage
        decryptor= cipher.decryptor()
        #Suppression du padding
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = decryptor.update(encrypted_messag)+decryptor.finalize()
         
        return (unpadder.update(plaintext)+unpadder.finalize())
    
    def send(self, text) -> None:
        message=self.encrypt(text)
        #function called to send a message to all (broadcasting)
        self._client.send_message(message)

    def recv(self) -> None:
        # function called to get incoming messages and display them
        if self._callback is not None:
            for user, message in self._callback.get():
                message = self.decrypt(message)
                self.update_text_screen(f"{user} : {message}")
            self._callback.clear()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = CipheredGUI()
    client.create()
    client.loop()