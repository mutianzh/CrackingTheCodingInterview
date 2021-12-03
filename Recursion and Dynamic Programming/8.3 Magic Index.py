"""
A magic index in an array A[ 1 .•. n-1] is defined to be an index such that A[ i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
"""
def find_magic_index(A):
    if not A:
        return -1
    return find_helper(A, 0, len(A) - 1)

def find_helper(A, low, high):
    if high < low:
        return -1

    mid = int((low + high)/2)
    if A[mid] == mid:
        return mid
    elif A[mid] < mid:
        return find_helper(A, mid + 1, high)
    else:
        return find_helper(A, low, mid - 1)

A = [-40,-20,-1,1,2,3,5,7,9,12,13]
print(find_magic_index(A))

# follow up: if values are not distinct

def find_magic_non_distinct(A):
    if not A:
        return -1
    return find_helper_non_distinct(A, 0, len(A) - 1)

def find_helper_non_distinct(A, low, high):
    if high < low:
        return -1
    mid = int((low + high) / 2)
    if A[mid] == mid:
        return mid

    else:
        if A[mid] < mid:
            # check all right side
            result = find_helper_non_distinct(A, mid + 1, high)
            if result > -1:
                return result
            else:
                # check partial left
                return find_helper_non_distinct(A, low, A[mid])

        else:
            # check all left
            result = find_helper_non_distinct(A, low, mid - 1)
            if result > -1:
                return result
            else:
                # check partial right
                return find_helper_non_distinct(A, A[mid], high)

A = [0, 0, 1, 2, 2, 3, 4, 4, 9, 10, 11]

print(find_magic_non_distinct(A))