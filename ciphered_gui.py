from basic_gui.py import BasicGUI

class CipheredGUI(BasicGUI):
    #Overrides of BasiGUI class to include self._key field
    def update(self, keys):
        self._key = None
    #Overrides _create_connection_window() to include password
    def _create_connection_window(self) -> None:
            with dpg.window(label="Connection", pos=(200, 150), width=400, height=300, show=False, tag="connection_windows"):
            
                for field in ["host", "port", "name"]:
                    with dpg.group(horizontal=True):
                        dpg.add_text(field)
                        dpg.add_input_text(default_value=DEFAULT_VALUES[field], tag=f"connection_{field}")
                dpg.add_text("Password")
                dpg.add_input_text(default_value=DEFAULT_VALUES["password"], tag=f"connection_{field}")
                dpg.add_button(label="Connect", callback=self.run_chat)