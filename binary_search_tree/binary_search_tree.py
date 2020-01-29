# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


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
        current_node = self

        while True:
            if current_node.right is not None:
                current_node = current_node.right
            elif current_node.right is None:
                return current_node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

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


new_tree = BinarySearchTree(5)
new_tree.insert(80)
new_tree.insert(90)
new_tree.insert(400)
max_value = new_tree.get_max()
