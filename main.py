from scripts.WindowsClickScript import WindowsClickScript
from src.scripts.ClickScript import ClickScript
from src.scripts.TestScript import TestScript

def run_test_script():
    machine = TestScript()
    machine.run_machine();

def run_click_script():
    machine = ClickScript()
    machine.run_machine();

def run_windows_script():
    machine = WindowsClickScript()
    machine.run_machine();

if __name__ == "__main__":
    #run_click_script();
    #run_test_script();
    run_windows_script();