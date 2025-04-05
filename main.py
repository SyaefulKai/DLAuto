from tkinter import *
from multiprocessing import Process
from pynput import keyboard
from NormalGate import run as normal_gate_run
from CharacterEventGate import run as character_gate_run


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("DLAuto")
        self.root.geometry("300x200")
        self.root.attributes("-topmost", True)
        self.root.columnconfigure(0, weight=1)

        self.process = None
        self.listener = None
        self.status_label = None 

        self.notice_frame = self.build_notice_frame("Press ESC to terminate the process", row=0)
        self.frame = self.build_main_frame()
        
        # Normal Gate Section
        self.normal_gate_status = self.build_new_gate_label(self.frame, row=1, col=1)
        self.normal_gate_button = self.build_new_gate_button(
            self.frame, "Normal Gate",
            lambda: self.activate_gate(normal_gate_run, self.normal_gate_status),
            row=1, col=0
        )
        
        # Character Gate Section
        self.character_gate_status = self.build_new_gate_label(self.frame, row=2, col=1)
        self.character_gate_button = self.build_new_gate_button(
            self.frame, "Character Event Gate",
            lambda: self.activate_gate(character_gate_run, self.character_gate_status),
            row=2, col=0
        )

    def build_notice_frame(self, text, col=0, row=0):
        notice_frame = Frame(self.root, borderwidth=5, relief="groove", width=300)
        notice_frame.grid(row=row, column=col, sticky="nsew")
        notice_frame.columnconfigure(0, weight=1)

        label = Label(notice_frame, text=text)
        label.grid(row=0, column=0, padx=10, pady=10)

        return notice_frame

    def build_main_frame(self):
        frame = Frame(self.root, borderwidth=5, relief="groove", width=300)
        frame.grid(row=1, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        return frame

    def build_new_gate_button(self, parent, text, command, col=0, row=0):
        button = Button(parent, text=text, command=command)
        button.grid(row=row, column=col, padx=10, pady=10, sticky="w")
        return button

    def build_new_gate_label(self, parent, row=0, col=0):
        label = Label(parent, text="Inactive")
        label.grid(row=row, column=col, padx=10, pady=10)
        return label

    def activate_gate(self, target, status_label=None):
        if self.process is None or not self.process.is_alive():
            self.status_label = status_label 
            self.status_label.config(text="Active")
            self.process = Process(target=target)
            self.process.start()
            self.listener = keyboard.Listener(on_press=self.on_key_press)
            self.listener.start()

    def on_key_press(self, key):
        if key == keyboard.Key.esc:
            self.deactivate_normal_gate()

    def deactivate_normal_gate(self):
        if self.process and self.process.is_alive():
            self.process.terminate()
            self.process = None
            print("Process terminated")

        if self.listener:
            self.listener.stop()
            self.listener = None

        if self.status_label: 
            self.status_label.config(text="Inactive")
            self.status_label = None


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
