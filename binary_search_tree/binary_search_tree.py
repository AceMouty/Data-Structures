import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self
        new_node_tree = None
        while True:
            if value < current_node.value and current_node.left is not None:
                current_node = current_node.left
            elif value > current_node.value and current_node.right is not None:
                current_node = current_node.right
            elif value < current_node.value and current_node.left is None:
                current_node.left = BinarySearchTree(value)
                new_node_tree = current_node.left
                break
            elif value > current_node.value and current_node.right is None:
                current_node.right = BinarySearchTree(value)
                new_node_tree = current_node.right
                break
        return new_node_tree

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        current_node = self

        while True:
            if target == current_node.value:
                return True
            elif target < current_node.value and current_node.left is None:
                return False
            elif target > current_node.value and current_node.right is None:
                return False
            elif target < current_node.value and current_node.left is not None:
                current_node = current_node.left
            elif target > current_node.value and current_node.right is not None:
                current_node = current_node.right

    # Return the maximum value found in the tree
    def get_max(self):
        # current_node = self

        # while True:
        #     if current_node.right is not None:
        #         current_node = current_node.right
        #     elif current_node.right is None:
        #         return current_node.value

        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    # THE FOR EACH IS A DEPTH FIRST SEARCH SETUP!
    def for_each(self, cb):
        # at a leaf node
        cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node=None):

        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # implement a queue
    def bft_print(self, node):
        bst_queue = Queue()
        bst_queue.enqueue(node)
        current_node = bst_queue.dequeue()

        while current_node:
            print(current_node.value)
            if current_node.right:
                bst_queue.enqueue(current_node.right)
            if current_node.left:
                bst_queue.enqueue(current_node.left)
            if bst_queue.size > 0:
                current_node = bst_queue.dequeue()
            else:
                break
            
        

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


# new_tree = BinarySearchTree(5)
# new_tree.insert(80)
# new_tree.insert(90)
# new_tree.insert(400)
# max_value = new_tree.get_max()
bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.in_order_print(bst)