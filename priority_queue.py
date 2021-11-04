# https://docs.python.org/2/library/sets.html

# Implementation of a priority queue that can be used for the frontier
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.record = set()

    # Adds an element into the queue, accounting for priority
    def push(self, priority, item):
        if tuple(item) not in self.record:
            self.queue.append((priority, item))
            self.heapify()
            self.record.add(tuple(item))

    # Removes top-most element in queue, and returns it
    def pop(self):
        return self.queue.pop(0)

    # Sorts the queue based on priority, imitating the behavior of a
    # priority queue
    # https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/
    def heapify(self):
        self.queue.sort(key=lambda x: x[0])

    # Removes the specified element in the queue
    def delete(self, item):
        if tuple(item) in self.record:
            for index, entry in enumerate(self.queue):
                if tuple(entry[1]) == tuple(item):
                    del self.queue[index]
                    self.record.remove(tuple(item))
                    self.heapify()

    # Changes the priority of a specified element in the queue
    def update(self, priority, item):
        if tuple(item) in self.record:
            for index, entry in enumerate(self.queue):
                if tuple(entry[1]) == tuple(item):
                    self.queue[index] = list(entry)
                    self.queue[index][0] = priority
                    self.queue[index] = tuple(self.queue[index])
                    self.heapify()
            
    # Prints the queue
    # Formatting: <priority> <item>
    def print_queue(self):
        for index, entry in enumerate(self.queue):
            print(entry[0], entry[1])