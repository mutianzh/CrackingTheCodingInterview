"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Input: "abcda"
Out: False

Input: "avd"
Ouptut: True

"""

def isUnique(string):
    if not string or len(string) == 0:
        return False
    seen = {}
    for s in string:
        if s in seen:
            return False
        else:
            seen[s] = True

    return True

inputs = ["abcda","avd",None,""]

for item in inputs:
    print(isUnique(item))
