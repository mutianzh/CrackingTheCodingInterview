"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false

"""

def one_way(s1, s2):

    if not s1 or not s2:
        return False

    len1 = len(s1)
    len2 = len(s2)

    if len1 == len2:
        return replace(s1, s2)

    if len1 == len2 + 1:
        return insert(s2, s1)

    if len2 == len1 + 1:
        return insert(s1, s2)


    return False

def insert(x1, x2):
    index1 = 0
    index2 = 0
    while index1 < len(x1):
        if x1[index1] == x2[index2]:
            index1 += 1
            index2 += 1
        else:
            if index1 != index2:
                return False
            else:
                index2 += 1

    return True

def replace(x1, x2):
    found_diff = False
    for i in range(len(x1)):
        if x1[i] != x2[i]:
            if found_diff:
                return False
            else:
                found_diff = True

    return True

"""
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
"""
inputs = [['pale', 'ple'], ['pales', 'pale'], ['pale', 'bale'], ['pale', 'bae'], [None, 'aa'], ['', 'a']]

for input in inputs:
    print(one_way(input[0], input[1]))
