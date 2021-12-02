"""
4.1O Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine ifT2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""
# solution 1:
def check_subtree(head_1, head_2):
    if not head_2:
        return True
    if not head_1:
        return False

    s1 = pre_order_string(head_1, '')
    s2 = pre_order_string(head_2, '')

    if s2 in s1:
        return True

    return False

def pre_order_string(node, s):
    if not node:
        return 'x'

    s += str(node.val)
    s += pre_order_string(node.left, s)
    s += pre_order_string(node.right, s)

    return s


# follow up: t1 is much larger than t2
def contains_tree(t1, t2):
    if not t2:
        return True
    return sub_tree(t1, t2)

def sub_tree(t1, t2):
    if not t1:
        return False
    if t1.val == t2.val and match_tree(t1, t2):
        return True

    else:
        return sub_tree(t1.left, t2) or sub_tree(t1.right, t2)

def match_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False

    return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)