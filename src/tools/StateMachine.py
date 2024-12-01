'''
Class to simulate a state machine
'''
class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def create_state(self, name, action):
        self.states[name] = action

    def run(self, state):
        while state and len(state) > 0:
            if state in self.states:
                print('Changing state to ' + state)
                self.current_state = state
                state = self.states[state]()
            else:
                raise Exception('No state called ' + state)

    def get_current_state(self):
        return self.current_state