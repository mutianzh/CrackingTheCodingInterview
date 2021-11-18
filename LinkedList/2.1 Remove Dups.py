"""
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

"""


def remove_duplicates(node):
    if node:
        seen = {}
        prev = node
        seen[prev.val] = True
        curr = node.next
        while curr:
            if curr.val in seen:
                # remove the curr from linked list
                prev.next = curr.next
            else:
                prev = curr
                seen[curr.val] = True

            curr = curr.next


    # Follow up: no extra space is allowed to use
    A = node
    val = A.val
    while A:
        B = A.next
        B_prev = A
        while B:
            if B.val == val:
                # delete node B and continue to next
                B_prev.next = B.next
            else:
                # continue to next
                B_prev = B

            B = B.next

        A = A.next
        val = A.val



