import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList(node=None)

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        
        # it follows the FIFO method
        self.storage = dll

    def enqueue(self, value):
        if self.storage.length < 1:
            return None
        if self.storage.length == 1:
            return 1
        self.storage.add_to_head(value)
        return self.storage.length

    def dequeue(self):
        if len(self.storage) > 1:
            return None
        return self.storage.remove_from_head()

    def len(self):
        return self.size
