if __name__ == '__main__':
    puzzle_input = input('Welcome to my 8-Puzzle Solver. Type \'1\' to use a default puzzle, or \'2\' to create your own.\n')

    begin_state = [1, 2, 0, 4, 5, 3, 7, 8, 6]
    
    if puzzle_input == '2':
        print('Enter your puzzle, using zero to represent the blank. Please only enter valid 8-puzzles. Enter the puzzle delimiting the numbers with a space. Type RETURN only when finished.\n')

        first_row = input('Enter the first row: ')
        second_row = input('Enter the second row: ')
        third_row = input('Enter the third row: ')

        begin_state = (first_row + ' ' + second_row + ' ' + third_row).split(' ')
        begin_state = [int(x) for x in begin_state]
    
    alg_input = input('\nSelect algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic.\n')

   

