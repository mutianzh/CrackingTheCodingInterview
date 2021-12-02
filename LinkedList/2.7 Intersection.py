"""
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""
import copy
def find_intersection(head_1, head_2):
    if not head_1 or not head_2:
        return None

    # find length and tail of each list:
    len_1, tail_1 = find_len_and_tail(head_1)
    len_2, tail_2 = find_len_and_tail(head_2)

    # Check if there is intersection
    if tail_1 != tail_2:
        return None

    # Find intersection
    # Chop the longer list
    K = abs(len_1 - len_2)
    longer = head_1 if len_1 >= len_2 else head_2
    shorter = head_1 if len_1 < len_2 else head_2
    while K > 0:
        longer = longer.next
        K -= 1

    # Find the intersection
    while longer != shorter:
        longer = longer.next
        shorter = shorter.next

    return longer

def find_len_and_tail(head):
    node = head
    len = 1
    while node.next:
        len += 1
        node = node.next

    return len, node

