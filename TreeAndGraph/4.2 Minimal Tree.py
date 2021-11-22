"""
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

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

def bfs_print(root):
    if not root:
        print(None)
        return
    print(root.val)
    queue = [root.left, root.right]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)

def dfs_print(root):
    if not root:
        return

    print(root.val)
    print(dfs_print(root.left))
    print(dfs_print(root.right))


L = [0,1,2,3,4,5,6,7]
root = minimal_tree(L)
#print(bfs_print(root))
print(dfs_print(root))





