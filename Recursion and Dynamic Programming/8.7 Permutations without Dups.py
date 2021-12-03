"""
Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.
"""


def permutations_without_dup(s):
    if not s:
        return None
    result = []
    perm_helper_without_dup('', s, result)
    return result

def perm_helper_without_dup(prefix, s, result):
    if len(s) == 0:
        result.append(prefix)
        return

    for i in range(len(s)):
        before = s[0: i]
        c = s[i]
        after = s[i + 1:]
        perm_helper_without_dup(prefix + c, before + after, result)


s = ''
print(permutations_without_dup(s))