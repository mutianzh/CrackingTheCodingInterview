"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""
def isPalindromePermutation(string):
    head = ord('a')
    bit_array = [0] * 26
    for c in string:
        index = ord(c) - head
        if index >= 0 and index < 26:
            if bit_array[index] == 0:
                bit_array[index] = 1
            else:
                bit_array[index] = 0

    num_ones = sum(bit_array)
    return not num_ones > 1

inputs = ['Tact Coa']

for s in inputs:
    print(isPalindromePermutation(s))