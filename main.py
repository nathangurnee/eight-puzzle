# Main file
from puzzle import Puzzle

if __name__ == '__main__':
    puzzle_input = input('Welcome to the 8-Puzzle Solver. Type \'1\' to use a default puzzle, or \'2\' to create your own.\n')

    start_state = [1, 2, 3, 4, 5, 6, 7, 0, 8] # Default state
    
    if puzzle_input == '2':
        print('Enter your puzzle, using zero to represent the blank. Please only enter valid 8-puzzles. Enter the puzzle delimiting the numbers with a space. Type RETURN only when finished.\n')

        first_row = input('Enter the first row: ')
        second_row = input('Enter the second row: ')
        third_row = input('Enter the third row: ')

        start_state = (first_row + ' ' + second_row + ' ' + third_row).split(' ')
        start_state = [int(x) for x in start_state]
    
    alg_input = input('\nSelect algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic.\n')

    puzzle = Puzzle(start_state, alg_input)
    puzzle.solve()