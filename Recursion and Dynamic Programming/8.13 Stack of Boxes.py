"""
8.13 Stack of Boxes: You have a stack of n boxes, with widths w1 , heights h i, and depths di . The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
"""

def find_max_height(boxes):
    boxes = sorted(boxes)
    n = len(boxes)
    dp = [0] * n
    dp[0] = boxes[0][1]

    for i in range(1, n):
        a, b, c = boxes[i]
        dp[i] = b
        for j in range(i):
            x, y, z = boxes[j]
            if x < a and y < b and z < c:
                dp[i] = max(dp[i], dp[j] + b)

    return max(dp)