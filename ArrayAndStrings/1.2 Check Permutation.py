"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""
import collections


def checkPerm(s1, s2):
    if not s1 or not s2 or len(s1) == 0 or len(s2) == 0:
        return False

    if len(s1) != len(s2):
        return False
    else:
        seen = collections.defaultdict(int)
        for s in s1:
            seen[s] += 1

        for s in s2:
            if seen[s] == 0:
                return False
            else:
                seen[s] -= 1

        return True



inputs = [["abc", "cba"], ["a bca", "aabc "], ["acfd", "sda"]]

for input in inputs:
    print(checkPerm(input[0], input[1]))