from src.tools.MouseController import MouseController
from src.tools.StateMachine import StateMachine
import time
import random

'''
Scrip that clicks every 30/50 seconds
'''
class ClickScript(StateMachine):
    def __init__(self):
         super().__init__()
         self.mouse_controller = MouseController()

    def waiting(self):
        delay = random.uniform(30, 50)
        print(f"Waiting for {delay:.2f} seconds before clicking...")
        time.sleep(delay)
        return 'click'
      
    def click(self):
        print("Click!")
        self.mouse_controller.left_click()
        time.sleep(0.3)
        self.mouse_controller.left_click()
        return 'waiting'

    def run_machine(self):
        self.create_state('click', self.click)
        self.create_state('waiting', self.waiting)
        self.run('waiting')
