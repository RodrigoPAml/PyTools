import pyautogui
import random
import time
import math

'''
Class to control the mouse
'''
class MouseController:
    def __init__(self):
        pass

    def _lerp(self, start, end, t):
        return start + (end - start) * t
    
    def _ease_in_out(self, t):
        return t * t * (3 - 2 * t)
    
    def _click(self, button='left'):
        pyautogui.click(button=button)

    def move_to(self, x, y, duration=1.0):
        start_x, start_y = pyautogui.position()
        
        steps = int(duration * 100)
        
        for step in range(steps + 1):
            t = step / float(steps)
            t = self._ease_in_out(t) 
            intermediate_x = self._lerp(start_x, x, t)
            intermediate_y = self._lerp(start_y, y, t)
            
            pyautogui.moveTo(intermediate_x, intermediate_y, duration=0, _pause=False)
            
            time.sleep(random.uniform(0.005, 0.015))
    
    def current_pos(self):
        start_x, start_y = pyautogui.position()
        return (start_x, start_y)

    def right_click(self):
        self._click(button='right')

    def left_click(self):
        self._click(button='left')