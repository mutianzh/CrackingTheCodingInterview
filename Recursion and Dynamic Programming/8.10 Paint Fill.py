"""
8.10 Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""
import numpy as np

def paint_fill(screen, o_color, n_color, r, c):
    if r < 0 or r > len(screen) - 1 or c < 0 or c > len(screen[0]) - 1:
        return False

    if o_color == n_color:
        return False

    if screen[r][c] == o_color:
        screen[r][c] = n_color
        paint_fill(screen, o_color, n_color, r - 1, c)
        paint_fill(screen, o_color, n_color, r + 1, c)
        paint_fill(screen, o_color, n_color, r, c - 1)
        paint_fill(screen, o_color, n_color, r, c + 1)

    return True


screen =   [['g', 'g', 'g', 'g', 'g', 'r'],
            ['g', 'g', 'g', 'g', 'r', 'r'],
            ['g', 'g', 'g', 'r', 'r', 'r'],
            ['g', 'g', 'r', 'r', 'r', 'r'],
            ['g', 'r', 'r', 'r', 'r', 'r'],
            ['r', 'r', 'r', 'r', 'r', 'r']]
r = 5
c = 5
paint_fill(screen, screen[r][c], 'b', r, c)

print(np.array(screen))