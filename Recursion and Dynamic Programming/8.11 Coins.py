"""
8.11 Coins: Given an infinite number of quarters (25 cents), dimes (1O cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""
#
# def make_change(n):
#     values = [25, 10, 5, 1]
#     map = [[0 for c in range(len(values))] for r in range(n + 1)]
#     return change_helper(n, 0, values, map)
#
# def change_helper(remaining, index, values, map):
#     if index >= len(values) - 1:
#         return 1
#
#     map_r = remaining
#     map_c = index
#     if map[map_r][map_c] > 0:
#         return map[remaining][index]
#     else:
#         i = 0
#         ways = 0
#         value = values[index]
#         while i * value <= remaining:
#             new_remaining = remaining - i * value
#             ways += change_helper(new_remaining, index + 1, values, map)
#             i += 1
#         map[map_r][map_c] = ways
#         return ways
#
# print(make_change(25))

class Solution:
    def change_top_down(self, amount, coins) -> int:
        if amount < 1 or len(coins) < 1:
            return 0
        # top down approach
        def find_change(remain, index, coins, seen):
            if index == len(coins) - 1:
                if remain % coins[index] == 0:
                    return 1
                else:
                    return 0

            if seen[remain][index] > -1:
                return seen[remain][index]

            i = 0
            ways = 0
            value = coins[index]
            while i * value <= remain:
                ways += find_change(remain - i * value, index + 1, coins, seen)
                i += 1

            seen[remain][index] = ways
            return seen[remain][index]

        seen = [[-1 for c in coins] for i in range(amount + 1)]
        return find_change(amount, 0, coins, seen)

    def change_bottom_up(self, amount, coins):
        # bottom up approach
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for m in range(1, amount + 1, 1):
                remain = m - c
                if remain >= 0:
                    dp[m] += dp[remain]

        return dp[amount]

sol = Solution()

print(sol.change_top_down(5, [1,2,5]))
print(sol.change_bottom_up(5, [1,2,5]))







