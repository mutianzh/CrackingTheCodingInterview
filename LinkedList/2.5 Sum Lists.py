"""
2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def add_one(node_1, node_2, carry):
    if not node_1 and not node_2 and carry == 0:
         return None

    if not node_1 and not node_2 and carry == 1:
        return Node(1)

    value = carry
    if node_1:
        value += node_1.val

    if node_2:
        value += node_2.val

    new_node = Node(value % 10)
    new_node.next = add_one(node_1.next, node_2.next, 1 if value >= 10 else 0)

    return new_node