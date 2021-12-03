"""
8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""

class solution:
    def find_path(self, maze):
        self.path = []
        self.failed = set()
        self.path_finder(maze, len(maze) - 1, len(maze[0]) - 1)
        return self.path

    def path_finder(self, maze, i, j):
        if i < 0 or j < 0 or not maze[i][j]:
            return False

        if (i,j) in self.failed:
            return False

        at_origin = i == 0 and j == 0
        if at_origin or self.path_finder(maze, i - 1, j) or self.path_finder(maze, i, j - 1):
            self.path.append([i, j])
            return True

        self.failed.add((i, j))
        return False

maze = [[True, True, True, True],[True, True, True, False],[True, False, False, True],[True, True, True, True]]

sol = solution()
print(sol.find_path(maze))

