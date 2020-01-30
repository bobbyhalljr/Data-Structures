import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root = Node(value)

    # 

    # Insert the given value into the tree
    def insert(self, value):
        # set curr_node pointer
        curr_node = self.root
        # if value is none, set value as root, return root
        if value is None:
            root = self.value
            return root
        # while loop / while current node
        while curr_node:
            # check if value is less than current node value
            if value < curr_node:
                # if current node left is none
                if curr_node.left is None:
                        # current node left equals Node()
                        curr_node.left = Node(value)
                        break
                # else current node is current node left
                else:
                    curr_node = curr_node.left
            # else 
            else:
                # if current node right is none
                if curr_node.right is None:
                    # current node right equals Node()
                    curr_node.right = Node(value)
                    break
                else:
                    # current node is current node right
                    curr_node = curr_node.right
      
      
        # init new node = ...
        # new_node = Node(value)
        # root = self.value
        # var - pointer - curr_node 
        # curr_node = value
        # while loop or recursion
        # if root.value < new_node:
        # 2x if less or greater than root 
        # 2x if / else 


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        else: 
            False

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
