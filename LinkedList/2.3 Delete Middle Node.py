"""
2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a ->b->d- >e- >f
"""

import copy

def remove_middle(node):
    # Copy the next node to the current node
    node.val = copy.deepcopy(node.next.val)
    # Remove the next node
    node.next = node.next.next