from Classes.Duel import Duel
from pynput import keyboard
import os


class Auto(Duel):
    def __init__(self):
        super().__init__()
        self.listener = keyboard.Listener(on_press=self.destroy_instance)
        self.listener.start()

    def destroy_instance(self, key):
        if key == keyboard.Key.esc:
            print("The code was stopped by the user.")
            os._exit(0)