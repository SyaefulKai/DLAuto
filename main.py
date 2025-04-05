from tkinter import *
from tkinter import ttk
from multiprocessing import Process
from pynput import keyboard

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("DLAuto")
        self.root.geometry("300x200")
        self.root.attributes("-topmost", True)
        self.root.columnconfigure(0, weight=1)
        
        self.listener = None
        
        self.frame = self.main_frame()
        self.normal_gate = self.normal_gate_button(self.frame, self.activate_normal_gate_bot)
        self.normal_gate_label = self.normal_gate_label(self.frame, "Inactive")
        
        
    def main_frame(self):
        frame = Frame(self.root, borderwidth=5, relief="groove", width=300)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        return frame
    
    def normal_gate_button(self, parent, action):
        button = Button(parent, text="Activate Normal Gate", command=action)
        button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        return button
    
    def activate_normal_gate_bot(self):
        self.normal_gate_label.config(text="Active")
        self.listener = keyboard.Listener(on_press=self.deactivate_normal_gate_bot)
        self.listener.start()
        
    def deactivate_normal_gate_bot(self, key):
        if key is keyboard.Key.esc:
            self.normal_gate_label.config(text="Inactive")
            self.listener.stop()
            return False
        
    def normal_gate_label(self, parent, text):
        label = Label(parent, text=text)
        label.grid(row=0, column=1, padx=10, pady=10)
        return label
        
        
    
            
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()