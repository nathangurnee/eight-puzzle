# https://docs.python.org/3/library/heapq.html
# https://docs.python.org/2/library/sets.html
# https://stackoverflow.com/questions/2831212/python-sets-vs-lists
# https://www.educative.io/edpresso/what-is-uniform-cost-search
import time
import heapq
from puzzle import Puzzle

def search(puzzle_state, search_algorithm):
    initial_time = time.time() # Initializes time
    frontier = [] # Priority queue of the states to be explored
    frontier_record = set() # Record of states in frontier queue
    states_seen = set() # The states already explored
    expanded_nodes = 0 # The number nodes whose children were explored

    # Creates a new Puzzle representing start state
    state = Puzzle(puzzle_state, search_algorithm)
    
    # Adds start state to the frontier
    heapq.heappush(frontier, (state.cost(list(state.start_state)), puzzle_state))
    frontier_record.add(tuple(list(state.start_state)))

    max_queue_size = len(frontier_record) # Most nodes the queue holds

    # Displays initial puzzle configuration
    state.display()

    while frontier:
        node = Puzzle(heapq.heappop(frontier)[1], search_algorithm)
        states_seen.add(tuple(list(node.current_state)))
        frontier_record.remove(tuple(list(node.current_state)))

        # Sets the new maximum queue size
        if len(frontier_record) > max_queue_size:
            max_queue_size = len(frontier_record)

        # Puzzle solved
        if node.current_state == node.goal_state:
            node.display()
            print('nodes expanded:', expanded_nodes)
            print('cpu time:', time.time() - initial_time, 'seconds')
            print('max queue size:', max_queue_size)
            return
        
        expanded_nodes += 1

        # Iterates over the children of the dequeued node
        # Ensures child has not already been expanded
        # and also is not already in the frontier
        # before adding it to the queue
        for child in node.children():
            if tuple(list(child.current_state)) not in frontier_record:
                if tuple(list(child.current_state)) not in states_seen:
                    heapq.heappush(frontier, (child.cost(list(child.current_state)), list(child.current_state)))

                    frontier_record.add(tuple(list(child.current_state)))
