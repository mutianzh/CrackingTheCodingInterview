"""
2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

def return_k_th_last(node, k):
    A = node
    B = node

    if not A:
        return None

    cnt = 0
    while cnt < k and B:
        B = B.next
        cnt += 1

    # The length of linked list is smaller than k, return None
    if cnt < k:
        return None

    while B:
        A = A.next
        B = B.next

    return A


