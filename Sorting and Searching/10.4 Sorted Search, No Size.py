"""
You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt ( i) method that returns the element at index i in
0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.
"""

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        no_value = 2 ** 31 - 1
        if reader.get(0) == no_value:
            return -1

        left = 0
        right = 1
        r_value = reader.get(right)
        while r_value < target and r_value != no_value:
            left = right
            right *= 2
            r_value = reader.get(right)

        # perform binary search between left and right index
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = reader.get(mid)
            if mid_value == target:
                return mid
            elif mid_value == no_value or mid_value > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1