
from collections import deque









s = open('input.txt','r').read().split('\n')








grid = []
for line in s:
    grid.append([i for i in line])


su = 0


for i in range(len(grid[0])):
    dq = deque()
    for j in range(len(grid)):
        if grid[j][i] == ".":
            dq.append((j,i))
        
        elif grid[j][i] == "O":
            if len(dq) > 0:
            
                newj,newi = dq.popleft()
                grid[newj][newi] = "O"
                su += len(grid) - newj
                grid[j][i] = "."
                dq.append((j,i))

            else:
                su += len(grid) - j
        
        elif grid[j][i] == "#":
            dq.clear()


print(su)



