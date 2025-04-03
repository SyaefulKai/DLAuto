from Classes.Finder import Finder
import pyautogui as gui

class Clicker(Finder):

    def clickCenterUntilFind(self, template, threshold = 0.8, max_attempt = 10, delay = 1, preprocess = True, modifier = [0, 0]):
        finder = Finder()
        while max_attempt > 0:
            coor = finder.find(template, threshold, preprocess)
            if coor is not None:
                coor[0] -= modifier[0]
                coor[1] -= modifier[1]
                gui.click(coor)
                return True
                break
            else:
                gui.click(self.getWindowCenter())
            max_attempt -= 1

    def clickCenter(self, amount, duration=0.2, modifier = [0, 0]):
        coordinate = self.getWindow().rectangle()
        for i in range(0, amount):
            gui.click([(coordinate.width() + modifier[0]) // 2, (coordinate.height() + modifier[1]) // 2], duration=duration)