"""
Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.
EXAMPLE
Input: ball, {"at","","","","","ball"}
Output: 4
"""


def sparse_search(Strings, target):
    if not Strings:
        return -1

    if target < Strings[0] or target > Strings[-1]:
        return -1

    left = 0
    right = len(Strings) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = Strings[mid]
        if mid_val == target:
            return mid

        if not mid_val:
            mid = first_non_empty(Strings, mid, left, right)
            if mid == -1:
                return -1

        if target < mid_val:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def first_non_empty(Strings, index, low, high):
    left = index - 1
    right = index + 1
    max = len(Strings) - 1
    while True:
        if left >= low and Strings[left]:
            return left

        elif right <= high and Strings[right]:
            return right

        if left < low and right > high:
            return -1

        left -= 1
        right += 1