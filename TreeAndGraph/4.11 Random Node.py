"""
4.11 Random Node: You are implementing a binary search tree class from scratch, which, in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
"""
from random import randrange

def random_node(root):
    if not root:
        return None
    choice = randrange(root.size)
    return find_ith_node(root, choice)

def find_ith_node(node, choice):
    if not node.left:
        left_size = 0
    else:
        lef_size = node.left.size

    if left_size == choice:
        return node
    elif left_size < choice:
        return find_ith_node(node.left, choice)
    else:
        return find_ith_node(node.right, choice - 1 - left_size)

