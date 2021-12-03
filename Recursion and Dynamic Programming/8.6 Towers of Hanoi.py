"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.
"""

class Tower:
    def __init__(self, i):
        self.index = i
        self.stack = []

    def add_disk(self, disk):
        if len(self.stack) > 0 and self.stack[-1] < disk:
            print('Error adding disk!')
        else:
            self.stack.append(disk)

    def move_top_to(self, destination):
        top_disk = self.stack.pop()
        destination.add_disk(top_disk)

    def move_disks_to(self, n, destination, buffer):
        if n > 0:
            self.move_disks_to(n-1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks_to(n-1, destination, self)


towers = []
for i in range(3):
    towers.append(Tower(i))

num_disk = 20
for disk in range(num_disk,0,-1):
    towers[0].add_disk(disk)

towers[0].move_disks_to(num_disk, towers[2], towers[1])

print(towers[0].stack)
print(towers[1].stack)
print(towers[2].stack)
