"""
4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node, cur_sum, targetSum, h):

            if not node:
                return

            # situation 1
            cur_sum += node.val
            if cur_sum == targetSum:
                self.count += 1

            # situation 2
            self.count += h[cur_sum - targetSum]

            # update prefix
            h[cur_sum] += 1

            # check left and right
            preorder(node.left, cur_sum, targetSum, h)
            preorder(node.right, cur_sum, targetSum, h)

            h[cur_sum] -= 1

        self.count = 0
        h = collections.defaultdict(int)
        preorder(root, 0, targetSum, h)

        return self.count