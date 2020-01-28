import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import Doubly_linked_list


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        ###  they follow the FIFO
        self.storage = Doubly_linked_list

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 1:
            return None
        return self.storage.delete()

    def len(self):
        return self.size
