"""
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
"""
import copy

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# solution 1: reverse the linked list
def is_palindrome(node):

    head_1 = copy.deepcopy(node)
    # clone a reversed linked list
    head_2 = None
    while node:
        clone_node = Node(node.val)
        clone_node.next = head_2
        head_2 = clone_node
        node = node.next

    # compare two list
    one = head_1
    two = head_2
    while one and two:
        if one.val != two.val:
            return False

        one = one.next
        two = two.next

    return True

# Solution: put half of list in stack
def is_palidrome_stack(node):
    if not node:
        return False

    # Put first half on linked list in stack
    stack = []
    slow = node
    fast = node
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        val = stack.pop()
        if val != slow.val:
            return False
        slow = slow.next

    return True


