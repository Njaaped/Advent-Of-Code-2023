from dataclasses import dataclass
import time

times = time.time()

def manhattan(node1,node2):
    return abs(node1.x-node2.x)+abs(node1.y-node2.y)

@dataclass
class Node:
    x:int
    y:int


s = open('input.txt','r').read().split('\n')
midgrid = []
for line in s:
    if all(char == "." for char in line):
        midgrid.append(line)
        midgrid.append(line)
    else:
        midgrid.append(line)

# for line in midgrid:
#     print(line)

grid = [[] for _ in range(len(midgrid))]
for i in range(len(midgrid[0])):
    col = []
    for j in range(len(midgrid)):
        col.append(midgrid[j][i])
    if all(char == "." for char in col):
        for j in range(len(midgrid)):
            grid[j].append(midgrid[j][i])
            grid[j].append(midgrid[j][i])
    else:
        for j in range(len(midgrid)):
            grid[j].append(midgrid[j][i])


nodes = []

for r, row in enumerate(grid):
    for c, ch in enumerate(grid[r]):
        if ch != ".":
            nodes.append(Node(r,c))

su = 0

for i, node in enumerate(nodes):
    for node2 in nodes[:i]:
        su += manhattan(node, node2)
    


print(su // 2)

print(time.time() - times)