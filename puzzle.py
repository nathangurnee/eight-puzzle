# Functionality of the puzzle

class Puzzle():
    def __init__(self, start_state, algorithm):
        self.start_state = start_state # Initial puzzle config
        self.current_state = start_state # Current puzzle config
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] # Goal config

        if (algorithm == '1'):
            self.algorithm = 'uniform cost'
        elif (algorithm == '2'):
            self.algorithm = 'misplaced tile'
        elif (algorithm == '3'):
            self.algorithm = 'manhattan distance'

        # Finds location of zero tile
        for index, tile in enumerate(self.current_state):
            if (tile == 0):
                self.zero_index = index

    # Swaps the zero tile with the desired tile
    # index_diff represents distance between zero tile and target tile
    def swap_tile(self, index_diff):
        target_index = self.zero_index + index_diff
        target_tile = self.current_state[target_index]
        self.current_state[target_index] = 0
        self.current_state[self.zero_index] = target_tile
        self.zero_index = target_index

    # Moves the zero tile up
    # Returns none if zero tile is in top row
    def move_up(self):
        if (self.zero_index == 0 or self.zero_index == 1 or self.zero_index == 2):
            return None
        self.swap_tile(-3)

    # Moves the zero tile down
    # Returns none if zero tile is in bottom row
    def move_down(self):
        if (self.zero_index == 6 or self.zero_index == 7 or self.zero_index == 8):
            return None
        self.swap_tile(3)

    # Moves the zero tile left
    # Returns none if zero tile is in left column
    def move_left(self):
        if (self.zero_index == 0 or self.zero_index == 3 or self.zero_index == 6):
            return None
        self.swap_tile(-1)

    # Moves the zero tile right
    # Return none if zero tile is in right column
    def move_right(self):
        if (self.zero_index == 2 or self.zero_index == 5 or self.zero_index == 8):
            return None
        self.swap_tile(1)

    # Shows the puzzle on each step
    def display(self):
        print('\n')
        print(self.current_state[0:3])
        print(self.current_state[3:6])
        print(self.current_state[6:9])

    # Handles solving the puzzle using selected algorithm
    def solve(self):
        if (self.algorithm == 'uniform cost'):
            print('uniform cost')
        elif (self.algorithm == 'misplaced tile'):
            print('misplaced tile')
        elif (self.algorithm == 'manhattan distance'):
            print('manhattan distance')
