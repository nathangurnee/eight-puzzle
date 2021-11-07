# Implementation of a priority queue that can be used for the frontier
class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Adds an element into the queue, accounting for priority
    def push(self, priority, item):
        if item not in self.queue:
            self.queue.append((priority, item))
            self.heapify()

    # Removes top-most element in queue, and returns it
    def pop(self):
        return self.queue.pop(0)

    # Sorts the queue based on priority, imitating the behavior of a
    # priority queue
    def heapify(self):
        self.queue.sort(key=lambda x: x[0])

    # Removes the specified element in the queue
    def delete(self, item):
        if item in self.queue:
            for index, entry in enumerate(self.queue):
                if tuple(entry[1]) == tuple(item):
                    del self.queue[index]
                    self.heapify()

    # Changes the priority of a specified element in the queue
    def update(self, priority, item):
        if item in self.queue:
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