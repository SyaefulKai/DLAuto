import pyautogui as gui
import pywinauto as window
from pywinauto import ElementNotFoundError

class Screen:

    def __init__(self):
        self.screenSize = gui.size()
        self.windowSize = self.getDLWindowSize()

    def getDLWindowSize(self):
        appName: str = "Yu-Gi-Oh! DUEL LINKS"
        try:
            DLInstance = window.Application().connect(title=appName)
            DLWindow = (DLInstance.top_window()).rectangle()
            return [DLWindow.width(), DLWindow.height()]
        except ElementNotFoundError as error:
            print(f"Please run {appName} first!")
            exit()

    def getWindowCenter(self):
        return [self.windowSize[0] // 2, self.windowSize[1] // 2]
    
    def getScreenCenter(self):
        return [self.screenSize[0] // 2, self.screenSize[1] // 2]