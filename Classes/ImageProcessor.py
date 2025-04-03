import cv2 as cv

class ImageProcessor:

    def grayscale(self, image):
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        return image

    def preprocess(self, image):
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        image = cv.GaussianBlur(image, (5, 5), 0)
        image = cv.Canny(image, 50, 150) 
        return image


    def preview(self, image):
        cv.imshow("Preview", image)
        cv.waitKey(0)
        cv.destroyAllWindows()
        