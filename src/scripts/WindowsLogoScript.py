import cv2
import time
import random
from src.tools.MouseController import MouseController
from src.tools.ScreenCapture import ScreenCapture
from src.tools.StateMachine import StateMachine
from src.tools.TemplateMatch import TemplateMatcher

'''
Script to match template the windows logo and display it
'''
class WindowsLogoScript(StateMachine):
    def __init__(self):
        super().__init__()
        self.mouse_controller = MouseController()
        self.frame_capture = ScreenCapture(1)
        self.find_windows = TemplateMatcher(r"src\resources\windows.png")

    def get_frame(self):
        return self.frame_capture.capture()

    def move_to_btn(self):
        frame = self.get_frame()

        matches = self.find_windows.match(frame, 0.9)
        
        if(len(matches) > 0):
            self.find_windows.draw_bounding_boxes(frame, matches)
        
            self.frame_capture.show(self.frame_capture.resize(frame, 800, 600))

            time.sleep(1/60)
            return 'move_to_btn'

    def run_machine(self):
        self.create_state('move_to_btn', self.move_to_btn)
        self.run('move_to_btn')