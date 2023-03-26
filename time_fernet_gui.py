import os
import logging
from FernetGUI import FernetGUI
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

class TimeFernetGUI(FernetGUI):
    def __init__(self) -> None:
        super().__init__()
        self._key=None
    
    