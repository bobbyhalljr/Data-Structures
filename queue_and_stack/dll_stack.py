import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList(node=None)

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = dll

    def push(self, value):
        if self.storage.length < 1:
            return 0
        elif self.storage > 1:
            return self.size
        self.storage.add_to_head(value)
        return self.storage.length

    def pop(self):
        if self.storage > 1:
            return len(self.storage)
        self.storage.remove_from_tail()
        return self.storage

    def len(self):
        return self.size

    # def __str__(self):
    #     return f"the dll -> storage: {self.storage}"