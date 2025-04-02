import pyautogui as gui
import pywinauto as window
from pywinauto import ElementNotFoundError

class Screen:
    
    def __init__(self):
        self.screenSize = gui.size()
        self.AppInstance = None

    @property
    def DLInstance(self):
        if self.AppInstance is None:
            appName = "Yu-Gi-Oh! DUEL LINKS"
            try:
                self.AppInstance = window.Application().connect(title=appName)
            except ElementNotFoundError:
                raise RuntimeError(f"Please run {appName} first!")
        return self.AppInstance

    def getWindowCenter(self):
        DLWindow = self.DLInstance.top_window().rectangle()
        return [(DLWindow.left + DLWindow.right) // 2, (DLWindow.top + DLWindow.bottom) // 2]
    
    def getScreenCenter(self):
        return [self.screenSize[0] // 2, self.screenSize[1] // 2]

