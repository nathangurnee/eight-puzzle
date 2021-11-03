# https://stackoverflow.com/questions/2831212/python-sets-vs-lists
# https://www.educative.io/edpresso/what-is-uniform-cost-search
import time
from priority_queue import PriorityQueue
from puzzle import Puzzle

def search(puzzle_state, search_algorithm):
    initial_time = time.time() # Initializes time
    frontier = PriorityQueue() # Priority queue of the states to be explored
    expanded_nodes = 0 # The number nodes whose children were explored

    # Record of states in frontier queue
    # Keys are puzzle states
    # Values are the states' depths in the tree
    frontier_record = {}

    # The states already explored
    # Same key-value pairs as the frontier record
    states_seen = {}

    # Creates a new Puzzle representing start state
    state = Puzzle(puzzle_state, search_algorithm)
    
    # Adds start state to the frontier
    frontier.push(state.cost(list(state.start_state)), puzzle_state)
    frontier_record[tuple(list(state.start_state))] = 0

    max_queue_size = len(frontier_record) # Most nodes the queue holds

    state.display() # Prints starting puzzle state

    print('solving...\n\n')

    while frontier:
        # Sets the new maximum queue size
        if len(frontier_record) > max_queue_size:
            max_queue_size = len(frontier_record)

        # Dequeues puzzle state to be looked at
        # Records puzzle state in the states that have already been seen
        node = Puzzle(frontier.pop()[1], search_algorithm)
        states_seen[tuple(list(node.current_state))] = frontier_record[tuple(list(node.current_state))]

        # Puzzle solved
        if node.current_state == node.goal_state:
            node.display()
            print('cpu time:', time.time() - initial_time, 'seconds')
            print('nodes expanded:', expanded_nodes)
            print('max queue size:', max_queue_size)
            print('solution depth:', frontier_record[tuple(list(node.current_state))])
            return

        # Iterates over the children of the dequeued node
        # Ensures child has not already been expanded
        # and also is not already in the frontier
        # before adding it to the queue
        for child in node.children():
            if tuple(list(child.current_state)) not in frontier_record:
                if tuple(list(child.current_state)) not in states_seen:
                    # Increases the node's depth in the tree
                    frontier_record[tuple(list(child.current_state))] = frontier_record[tuple(list(node.current_state))] + 1
                    
                    # The total cost of the node, f(n), is equal to its
                    # depth + its heuristic value
                    node_cost = frontier_record[tuple(list(child.current_state))] + child.cost(list(child.current_state))

                    # Adds the puzzle state and its cost to the frontier
                    frontier.push(node_cost, list(child.current_state))
            else:
                # Heuristic value for the child node
                h_n = child.cost(list(child.current_state))

                if tuple(list(child.current_state)) in frontier_record:
                    # Old cost is the heuristic + the original depth
                    old_cost = frontier_record[tuple(list(child.current_state))] + h_n

                    # New cost is the heuristic + the new depth
                    new_cost = (frontier_record[tuple(list(node.current_state))] + 1) + h_n

                    # Uses the identical node and its better cost in place of
                    # the old node
                    if new_cost < old_cost:
                        frontier.update(new_cost, list(child.current_state))
                elif tuple(list(child.current_state)) in states_seen:
                    old_cost = states_seen[tuple(list(child.current_state))] + h_n
                    new_cost = (states_seen[tuple(list(node.current_state))] + 1) + h_n
                    
                    # Puts node back in frontier if its new cost is better than # its old cost
                    if new_cost < old_cost:
                        frontier.push(new_cost, list(child.current_state))
                        frontier_record[tuple(list(child.current_state))] = new_cost
                        del states_seen[tuple(list(child.current_state))]

        # Removes puzzle state from the record of the frontier
        del frontier_record[tuple(list(node.current_state))]

        expanded_nodes += 1 # Found all children of the first node in frontier