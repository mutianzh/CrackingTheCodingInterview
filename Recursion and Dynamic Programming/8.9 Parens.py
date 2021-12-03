"""
8.9 Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: (( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
"""

def print_all_valid_pars(n):
    if not n > 0:
        print('')
        return
    print_helper(n*2, 0, '')

def print_helper(num_left, sum, prefix):
    if sum < 0:
        return

    if num_left == 0:
        if sum == 0:
            print(prefix)
        return
    else:
        print_helper(num_left - 1, sum + 1, prefix + '(')
        print_helper(num_left - 1, sum - 1, prefix + ')')

print_all_valid_pars(4)
