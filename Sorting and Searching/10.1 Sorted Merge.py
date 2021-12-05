"""
10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""

def merge_sort(A, B, last_A, last_B):
    end_index = -1

    while last_A >= 0 or last_B >= 0:
        if last_A >= 0 and last_B >= 0:
            a = A[last_A]
            b = B[last_B]

            if a < b:
                A[end_index] = b
                last_B -= 1
            else:
                A[end_index] = a
                last_A -= 1

        elif last_A >= 0:
            a = A[last_A]
            A[end_index] = a
            last_A -= 1
        else:
            b = B[last_B]
            A[end_index] = b
            last_B -= 1

        end_index -= 1



A = [1,4,6,7,None,None,None]
B = [2,3,8]

merge_sort(A, B, 3, 2)
print(A)