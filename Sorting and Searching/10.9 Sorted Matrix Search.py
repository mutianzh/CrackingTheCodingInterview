"""
Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element
"""


class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        def binary_search(target, left, right, L):
            while left <= right:
                mid = left + (right - left) // 2
                if L[mid] == target:
                    return mid
                elif L[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return right

        M = len(matrix)  # num of rows
        N = len(matrix[0])  # num of cols
        row = 0
        col_l = 0
        col_r = N - 1

        if not matrix or target < matrix[0][0] or target > matrix[M - 1][N - 1]:
            return False

        while True:
            if row >= M or col_r < 0:
                break

            if matrix[row][0] > target:
                break

            if matrix[row][col_r] >= target:
                col_r = binary_search(target, 0, col_r, matrix[row])
                if matrix[row][col_r] == target:
                    return True

            row += 1

        return False

solution = Solution()

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

print(solution.searchMatrix(matrix, target))
