from Classes.Screen import Screen
from Classes.ImageProcessor import ImageProcessor
import numpy as np
import cv2 as cv

class Finder(Screen, ImageProcessor):

    def find(self, template, threshold=0.8, preprocess = True):
        """
        Match given template with screenshot of Duel Links instance

        Parameters
        ----------
        template: str
            path to template
        threshold: int
        preprocess: boolean
            Preprocess the template and screenshot to improve its accuracy
        """
        screenshot = np.copy(self.captureWindow())

        target = cv.imread(template, cv.IMREAD_GRAYSCALE)

        if preprocess is True:
            screenshot = self.preprocess(screenshot)
            target = self.preprocess(target)

        result = cv.matchTemplate(screenshot, target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val < threshold:
            print(f"Accuracy is too low: {round(max_val)} ({template})")
            return None  
 
        w, h = target.shape[::-1]

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(screenshot, top_left, bottom_right, (255, 255, 255), 10)

        return [top_left[0] + (w // 2), top_left[1] + (h // 2)]