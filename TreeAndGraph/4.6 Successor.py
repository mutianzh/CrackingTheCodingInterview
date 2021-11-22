"""
4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""

def find_successor(Node):
    if not Node:
        return None

    if Node.right:
        # find left most child of the right subtree
        return find_most_left(Node.right)

    n = Node
    p = n.parent
    while p and p.left != n:
        n = p
        p = n.parent

    return p


def find_most_left(Node):
    x = Node
    while x.left:
        x = x.left

    return x