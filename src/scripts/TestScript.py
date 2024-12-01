from src.tools.StateMachine import StateMachine

'''
Script to test
'''
class TestScript(StateMachine):
    def __init__(self):
         super().__init__()

    def initial(self):
        print("initial")
        return 'final'

    def final(self):
        print("final")

    def run_machine(self):
        self.create_state('initial', self.initial)
        self.create_state('final', self.final)
        self.run('initial')
