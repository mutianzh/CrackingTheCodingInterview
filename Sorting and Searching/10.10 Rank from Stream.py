"""
Imagine you are reading in a stream of integers. Periodically, you wish
to be able to look up the rank of a number x (the number of values less than or equal to x).
Implement the data structures and algorithms to support these operations. That is, implement
the method track(int x), which is called when each number is generated, and the method
getRankOfNumber(int x), which returns the number of values less than or equal to x (not
including x itself).
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.left_count = 0

def insert(root, value):
    if not root:
        return Node(value)

    root_val = root.value
    if root_val < value:
        insert(root.right, value)
    else:
        insert(root.left, value)
        root.left_count += 1

def get_rank(root, value):
    if not root:
        return -1

    if root.val == value:
        return root.left_count
    elif root.val < value:
        return get_rank(root.right, value)
    else:
        res = get_rank(root.left, value)
        if res == -1:
            return -1
        else:
            # root and root's left sub tree all smaller than value
            return res + root.left_count