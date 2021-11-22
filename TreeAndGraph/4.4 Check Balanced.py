"""
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""


# Generate a tree
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

def minimal_tree(L):
    def find_root(A, start, end):
        if not A:
            return None

        if end < start:
            return None

        mid = int((start + end) / 2)
        root = Node(A[mid])
        root.left = find_root(A, start, mid - 1)
        root.right = find_root(A, mid + 1, end)
        return root

    return find_root(L, start = 0, end = len(L) - 1)

L = [0,1,2,3,4,5,6,7]
root = minimal_tree(L)



class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

error_code = "error"

def find_height(Node):
    if not Node:
        return -1

    height_left = find_height(Node.left)
    if height_left == error_code:
        return error_code

    height_right = find_height(Node.right)
    if height_right == error_code:
        return error_code

    diff = abs(height_right - height_left)
    if diff > 1:
        return error_code
    else:
        return max(height_right, height_left) + 1


def is_balanced(Node):
    if find_height(Node) == error_code:
        return False
    return True

print(is_balanced(root))