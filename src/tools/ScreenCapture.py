import datetime
import mss
import numpy as np
import cv2
from screeninfo import get_monitors

'''
Class to capture frames and manipulate it
'''
class ScreenCapture:
    def __init__(self, screen_number=1):
        self.screen_number = screen_number
        self.monitors = get_monitors()
        
        monitor = self.monitors[self.screen_number - 1]
        self.screen_area = {
            "top": monitor.y,
            "left": monitor.x,
            "width": monitor.width,
            "height": monitor.height
        }

    def capture(self):
        with mss.mss() as sct:
            screenshot = sct.grab(self.screen_area)
            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            return img

    def resize(self, frame, width, height):
        return cv2.resize(frame, (width, height))

    def show(self, frame):
        cv2.imshow(f'Tela {self.screen_number}', frame)

        key = cv2.waitKey(1)
        if key == 27:
            exit(0)

    def save_frame(self, frame, filename=None):
        if filename is None:
            filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
        
        cv2.imwrite(filename, frame)