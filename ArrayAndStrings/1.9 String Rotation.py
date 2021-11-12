"""
1.9 String Rotation: Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat").
"""

def is_rotation(s1, s2):
    if not s1 or not s2:
        return False

    if len(s1) == len(s2) and len(s1) > 0:
        return s2 in s1 + s1

    return False

inputs = [['waterbottle', 'erbottlewat'], ['asdas','ssdas'], [None, 'a'], ['', 's'], ['ass', 'ssa']]

for input in inputs:
    print(is_rotation(input[0], input[1]))