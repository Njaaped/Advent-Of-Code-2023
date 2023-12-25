from dataclasses import dataclass
import time 

times = time.time()

def manhattan(node1,node2,col,row):
    ekstra = 0
    for i in range(min(node1.x,node2.x), max(node1.x,node2.x)):
        if i in row:
            ekstra += 1_000_000 - 1 
 
    for i in range(min(node1.y,node2.y), max(node1.y,node2.y)):
        if i in col:
            ekstra += 1_000_000 - 1 


    return abs(node1.x-node2.x)+abs(node1.y-node2.y) + ekstra

@dataclass
class Node:
    x:int
    y:int

s = open('input.txt','r').read().split('\n')
midgrid = []

columns = set()
rows = set()

for ind, line in enumerate(s):
    if all(char == "." for char in line):
        midgrid.append(line)
        rows.add(ind)

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

        columns.add(i)
    else:
        for j in range(len(midgrid)):
            grid[j].append(midgrid[j][i])


nodes = []

for r, row in enumerate(grid):
    for c, ch in enumerate(grid[r]):
        if ch != ".":
            nodes.append(Node(r,c))

su = 0
checked = set()
for i, node in enumerate(nodes):
    for node2 in nodes[:i]:
        su += manhattan(node,node2, columns, rows)

print(su)

print(time.time() - times)