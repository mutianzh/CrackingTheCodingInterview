"""
8.8 Permutations with Duplicates: Write a method to compute all permutations of a string whose
characters are not necessarily unique. The list of permutations should not have duplicates.
"""
def permutation_with_dup(s):
    result = []
    helper_with_dub('', s, result)
    return result

def helper_with_dub(prefix, s, result):
    if len(s) == 0:
        result.append(prefix)
        return

    seen = set()
    for i in range(len(s)):
        c = s[i]
        if c not in seen:
            seen.add(c)
            before = s[0:i]
            after = s[i+1:]
            helper_with_dub(prefix + c, before + after, result)


s = ''
print(permutation_with_dup(s))