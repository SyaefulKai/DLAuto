from Classes.Finder import Finder
import pyautogui as gui

class Clicker(Finder):

    def clickCenterUntilFind(self, template, threshold = 0.8, max_attempt = 10, delay = 1, preprocess = True, modifier = [0, 0]):

        while max_attempt > 0:
            coor = self.find(template, threshold, preprocess)
            if coor is not None:
                gui.click(coor)
                return True
                break
            else:
                center = self.getWindowCenter()
                center[0] -= modifier[0]
                center[1] -= modifier[1]
                print(center)
                gui.click(center)
            max_attempt -= 1

    def clickCenter(self, amount, duration=0.2, modifier = [0, 0]):
        coordinate = self.getWindow().rectangle()
        for i in range(0, amount):
            gui.click([(coordinate.width() + modifier[0]) // 2, (coordinate.height() + modifier[1]) // 2], duration=duration)
