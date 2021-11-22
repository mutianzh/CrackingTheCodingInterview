"""
4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists)
"""

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


def depth_dfs(Node):
    result_list = []
    def dfs(Node, level, list):
        if not Node:
            return

        if level <= len(list):
            # append to exist linked list
            list[level - 1].next = ListNode(Node.val)
        else:
            # start a new linked list
            list.append(ListNode(Node.val))
        dfs(Node.left, level + 1, list)
        dfs(Node.right, level + 1, list)


    dfs(Node, 1, result_list)
    return result_list


import copy

def depth_bfs(Node):
    if not Node:
        return None
    current = [Node]
    result_list = []
    next = []
    while current:
        for i in range(len(current)):
            # Append the node to linked list
            if i == 0:
                # create a new linked list node
                result_list.append(ListNode(current[i].val))
            else:
                # append to the last linked list
                result_list[-1].next = ListNode(current[i].val)

            # Append children to next list
            if current[i].left:
                next.append(current[i].left)
            if current[i].right:
                next.append(current[i].right)

        current = copy.deepcopy(next)
        next = []

    return result_list

L = [0, 1, 2, 3, 4, 5, 6, 7]
root = minimal_tree(L)

result = depth_bfs(root)
for node in result:
    print(node.val)