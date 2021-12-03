"""
8.11 Coins: Given an infinite number of quarters (25 cents), dimes (1O cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""

def make_change(n):
    values = [25, 10, 5, 1]
    map = [[0 for c in range(len(values))] for r in range(n + 1)]
    return change_helper(n, 0, values, map)

def change_helper(remaining, index, values, map):
    if index >= len(values) - 1:
        return 1

    map_r = remaining
    map_c = index
    if map[map_r][map_c] > 0:
        return map[remaining][index]
    else:
        i = 0
        ways = 0
        value = values[index]
        while i * value <= remaining:
            new_remaining = remaining - i * value
            ways += change_helper(new_remaining, index + 1, values, map)
            i += 1
        map[map_r][map_c] = ways
        return ways

print(make_change(25))







