
from collections import deque



def rollalldir(grid):

    #north
    for i in range(len(grid[0])):
        dq = deque()
        for j in range(len(grid)):
            if grid[j][i] == ".":
                dq.append((j,i))
            
            elif grid[j][i] == "O":
                if len(dq) > 0:
                
                    newj,newi = dq.popleft()
                    grid[newj][newi] = "O"

                    grid[j][i] = "."
                    dq.append((j,i))


            
            elif grid[j][i] == "#":
                dq.clear()
    

    #west
    for i in range(len(grid)):
        dq = deque()
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                dq.append((i,j))
            
            elif grid[i][j] == "O":
                if len(dq) > 0:
                
                    newi,newj = dq.popleft()
                    grid[newi][newj] = "O"
    
                    grid[i][j] = "."
                    dq.append((i,j))

            
            elif grid[i][j] == "#":
                dq.clear()


    #soutj
    for i in range(len(grid[0])):
        dq = deque()
        for j in range(len(grid)-1,-1,-1):
            if grid[j][i] == ".":
                dq.append((j,i))
            
            elif grid[j][i] == "O":
                if len(dq) > 0:
                
                    newj,newi = dq.popleft()
                    grid[newj][newi] = "O"

                    grid[j][i] = "."
                    dq.append((j,i))


            
            elif grid[j][i] == "#":
                dq.clear()
    

    # easy
    for i in range(len(grid)):
        dq = deque()
        for j in range(len(grid[0])-1,-1,-1):
            if grid[i][j] == ".":
                dq.append((i,j))
            
            elif grid[i][j] == "O":
                if len(dq) > 0:
                
                    newi,newj = dq.popleft()
                    grid[newi][newj] = "O"
    
                    grid[i][j] = "."
                    dq.append((i,j))

            
            elif grid[i][j] == "#":
                dq.clear()

    return grid

s = open('input.txt','r').read().split('\n')


grid = []
for line in s:
    grid.append([i for i in line])

sets = set()
li = []

for i in range(1,1001):
    grid = rollalldir(grid)
    tupgrid = tuple(tuple(i for i in grid[j]) for j in range(len(grid)))
   
    if tupgrid in sets:
        print(li.index(tupgrid))
        print(i)
    else:
        sets.add(tupgrid)
        li.append(tupgrid)

ans = li[108]

su = 0
for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] == "O":
            su += len(ans) - i

print(su)
# print(1000000000%27)

