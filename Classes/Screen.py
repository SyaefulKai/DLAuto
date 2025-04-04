import pyautogui as gui
import pywinauto as window
from pywinauto import ElementNotFoundError
import mss
import numpy as np
import cv2 as cv

class Screen:

    def __init__(self):
        self.screenSize = gui.size()
        self._DLInstance = self.getInstance()

    def getInstance(self):
        appName = "Yu-Gi-Oh! DUEL LINKS"
        try:
            return window.Application().connect(title=appName)
        except ElementNotFoundError as error:
            raise RuntimeError(f"Could not connect to {appName}. Please ensure the application is running.") from error

    def getRunningInstance(self):
        return self._DLInstance

    def getWindowCenter(self):
        if self._DLInstance is None:
            raise RuntimeError("Duel Links is not connected! Cannot get window center.")

        DLWindow = self.getWindow().rectangle()
        return [(DLWindow.left + DLWindow.right) // 2, (DLWindow.top + DLWindow.bottom) // 2]

    def getScreenCenter(self):
        return [self.screenSize[0] // 2, self.screenSize[1] // 2]

    def getWindow(self):
        if self._DLInstance is None:
            raise RuntimeError("Duel Links is not connected! Cannot get window.")

        return self._DLInstance.top_window()

    def captureWindow(self, grayscale = False):
        
        window = self.getWindow()
        rectangle = window.rectangle()

        # It will open Duel Links
        window.set_focus()

        monitor = {
            "left": rectangle.left,
            "top": rectangle.top,
            "width": rectangle.width(),
            "height": rectangle.height()
        }

        with mss.mss() as sct:
            screenshot = sct.grab(monitor)
            image = np.frombuffer(screenshot.rgb, dtype=np.uint8)
            image = image.reshape((screenshot.height, screenshot.width, 3))
            image = np.ascontiguousarray(image, dtype=np.uint8)
            return image