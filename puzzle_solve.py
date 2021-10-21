# PuzzleSolve class responsible for handling solving functionality

class PuzzleSolve:
    def __init__(self, start_state, goal_state, algorithm):
        self.start_state = start_state  # Sets starting puzzle state

        if (algorithm == '1'):
            self.algorithm = uniform_cost_search
        elif (algorithm == '2'):
            self.algorithm = misplaced_tile
        elif(algorithm == '3'):
            self.algorithm = manhattan


