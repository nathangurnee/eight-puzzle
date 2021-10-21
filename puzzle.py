# Functionality of the puzzle

class Puzzle():
    def __init__(self, start_state, algorithm):
        self.start_state = start_state # Initial puzzle config
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] # Goal config

        if (algorithm == '1'):
            self.algorithm = 'uniform cost'
        elif (algorithm == '2'):
            self.algorithm = 'misplaced tile'
        elif (algorithm == '3'):
            self.algorithm = 'manhattan distance'

    # Shows the puzzle on each step
    def display(self):
        pass

    # Handles solving the puzzle using selected algorithm
    def solve(self):
        if (self.algorithm == 'uniform cost'):
            print('uniform cost')
        elif (self.algorithm == 'misplaced tile'):
            print('misplaced tile')
        elif (self.algorithm == 'manhattan distance'):
            print('manhattan distance')
