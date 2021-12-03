"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""

def count_ways(n):
    if not n or n < 0:
        return 0
    memo = [-1] * (n + 1)
    memo[0] = 1
    return count_helper(n, memo)


def count_helper(n, memo):
    if n < 0:
        return 0
    else:
        if memo[n] > -1:
            return memo[n]
        else:
            memo[n] = count_helper(n - 1, memo) + count_helper(n - 2, memo) + count_helper(n - 3, memo)
            return memo[n]


print(count_ways(3))
