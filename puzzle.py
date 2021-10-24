import time
import heapq

# Functionality of the puzzle
class Puzzle():
    def __init__(self, start_state, algorithm):
        self.start_state = start_state # Initial puzzle config
        self.current_state = start_state # Current puzzle config
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] # Goal config
        self.child_states = [] # Children of current state

        if algorithm == '1':
            self.algorithm = 'uniform cost'
        elif algorithm == '2':
            self.algorithm = 'misplaced tile'
        elif algorithm == '3':
            self.algorithm = 'manhattan distance'

        # Finds location of zero tile
        for index, tile in enumerate(self.current_state):
            if tile == 0:
                self.zero_index = index

    # Swaps the zero tile with the desired tile
    # index_diff Distance between zero tile and target tile
    def swap_tile(self, index_diff):
        target_index = self.zero_index + index_diff
        target_tile = self.current_state[target_index]
        self.current_state[target_index] = 0
        self.current_state[self.zero_index] = target_tile
        self.zero_index = target_index

    # Moves the zero tile up
    # Returns none if zero tile is in top row
    def move_up(self):
        if self.zero_index < 3:
            return None
        self.swap_tile(-3)

    # Moves the zero tile down
    # Returns none if zero tile is in bottom row
    def move_down(self):
        if self.zero_index > 5:
            return None
        self.swap_tile(3)

    # Moves the zero tile left
    # Returns none if zero tile is in left column
    def move_left(self):
        if self.zero_index == 0 or self.zero_index == 3 or self.zero_index == 6:
            return None
        self.swap_tile(-1)

    # Moves the zero tile right
    # Return none if zero tile is in right column
    def move_right(self):
        if self.zero_index == 2 or self.zero_index == 5 or self.zero_index == 8:
            return None
        self.swap_tile(1)

    # Calculates the cost of a puzzle state
    def cost(self, state):
        state_cost = 0
        if self.algorithm == 'uniform cost':
            pass # The cost of each node is the same
        elif self.algorithm == 'misplaced tile':
            # Keeps track of number of misplaced tiles
            for index, tile in enumerate(state):
                if tile != self.goal_state[index]:
                    state_cost += 1
        elif self.algorithm == 'manhattan distance':
            # Sum of manhattan distance of all tiles
            for index, tile in enumerate(state):
                # Uses manhattan distance formula
                state_cost += abs(index // 3 - self.goal_state.index(tile) // 3) + abs(index % 3 - self.goal_state.index(tile) % 3)
        return state_cost

    # Finds all possible children of the current puzzle state
    def children(self):
        # Keeps track of current state configuration
        original_state = list(self.current_state)

        # Moves zero piece
        # Adds to child list if it is not the parent
        # The current state gets reassigned to the state before the move
        self.move_up()
        if list(self.current_state) != original_state:
            self.child_states.append(list(self.current_state))
            for index, tile in enumerate(original_state):
                self.current_state[index] = tile
            self.zero_index = original_state.index(0)

        self.move_down()
        if list(self.current_state) != original_state:
            self.child_states.append(list(self.current_state))
            for index, tile in enumerate(original_state):
                self.current_state[index] = tile
            self.zero_index = original_state.index(0)

        self.move_left()
        if list(self.current_state) != original_state:
            self.child_states.append(list(self.current_state))
            for index, tile in enumerate(original_state):
                self.current_state[index] = tile
            self.zero_index = original_state.index(0)

        self.move_right()
        if list(self.current_state) != original_state:
            self.child_states.append(list(self.current_state))
            for index, tile in enumerate(original_state):
                self.current_state[index] = tile
            self.zero_index = original_state.index(0)

        return self.child_states

    # Shows the puzzle on each step
    # time The amount of time the algorithm took to finish
    # nodes The total number of nodes explored
    # size The max queue size during the algorithm
    def display(self):
        print('\n')
        print(self.current_state[0:3])
        print(self.current_state[3:6])
        print(self.current_state[6:9])

    # Handles solving the puzzle using selected algorithm
    def solve(self):
        initial_time = time.time() # Initializes time
        frontier = [] # The states to be explored
        states_seen = set() # The states already explored
        
        heapq.heappush(frontier, (self.cost(self.start_state), self.start_state))
        for i in range(0, 10):
            self.current_state = heapq.heappop(frontier)[1]
            states_seen.add(tuple(self.current_state))
            self.display()

            if self.current_state != self.goal_state:
                for child in self.children():
                    heapq.heappush(frontier, (self.cost(child), child))

            i += 1

                
                







        final_time = time.time() - initial_time # Time to find goal state
