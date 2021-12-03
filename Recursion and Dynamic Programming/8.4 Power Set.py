"""
Write a method to return all subsets of a set.
"""

def find_power_set(A):
    if not A:
        return []
    power_set = []
    find_helper(0, A, [], power_set)
    return power_set


def find_helper(i, A, subset, power_set):
    if i == len(A):
        power_set.append(subset)
    else:
        new_subset = list(subset)
        new_subset.append(A[i])
        find_helper(i + 1, A, new_subset, power_set)
        find_helper(i + 1, A, subset, power_set)
    return

A = ['a', 'b', 'c']
print(find_power_set(A))