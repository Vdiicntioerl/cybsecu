import os
import logging
from ciphered_gui import CipheredGUI
from chat_client import ChatClient
from cryptography.fernet import Fernet
import dearpygui.dearpygui as dpg
import hashlib
import base64
from generic_callback import GenericCallback

DEFAULT_VALUES = {
    "host" : "127.0.0.1",
    "port" : "6666",
    "name" : "foo",
    "password" : ""
}
class FernetGUI(CipheredGUI):
    def __init(self) -> None:
        super().__init__()
        self._key =None

    def key_derivation(self, password: str) -> bytes:
        #Hashage du mot de passe puis recuperation de l'empreinte
        key=hashlib.sha256(password.encode()).digest()
        key = base64.b64encode(key)
        return key
    

    def run_chat(self, sender, app_data) -> None:
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
        f=Fernet(self._key)
        encrypted_message=f.encrypt(bytes(message,'utf-8'))
        return encrypted_message
    
    def decrypt(self, encrypted_message):
        message = base64.b64decode(encrypted_message['data'])
        f = Fernet(self._key)
        message = f.decrypt(message).decode()
        return message
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = FernetGUI()
    client.create()
    client.loop()    

