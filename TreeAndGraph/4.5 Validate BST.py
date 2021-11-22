"""
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""

last_printed = None
def validate_in_order(Node):
    if not Node:
        return True

    global last_printed

    if not validate_in_order(Node.left):
        return False

    if last_printed and last_printed >= Node.val:
        return False

    last_printed = Node.val

    if not validate_in_order(Node.right):
        return False

    return True


def validate_min_max(Node, min, max):
    if not Node:
        return True

    if min and Node.val <= min:
        return False

    if max and Node.val >= max:
        return False

    return validate_min_max(Node.left,min,Node.val) and validate_min_max(Node.right, Node.val, max)

