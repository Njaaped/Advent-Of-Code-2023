

from collections import deque
from dataclasses import dataclass


@dataclass
class Point:
    x:int
    y:int
    s:int
    v:set
    ld:tuple
    def __hash__(self) -> int:
        return tuple(self.x,self.y)
    

@dataclass
class Edge:
    fr:tuple
    to:tuple
    l:int




def getedges(g, start, end):
    visited = set()
    visited.add((start.x,start.y))
    q = deque([(start.x,start.y)])
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    adjset = {(start.x,start.y) : []}
    while q:
        x,y = q.pop()
        adjcount = 0
        for dir in dirs:
            newx,newy = x+dir[0],y+dir[1]
            if 0<=newx<len(g) and 0<= newy < len(g[0]) and g[newx][newy] != "#":
                adjcount += 1
                if (newx,newy) not in visited:
                    q.append((newx,newy))
                    visited.add((newx,newy))


def rightdir(dir, letter):
    dirs = [(-1,0), (0,1),(1,0),(0,-1)]
    lets = ["^", ">", "v", "<"]
    if letter not in lets:
        return True
    
    if lets.index(letter) == dirs.index(dir):
        return True
    
    return False


def checkgreater(newx,newy,news,newg,dir):
    if len(newg[newx][newy]) == 0:
        return True

    for elem in newg[newx][newy]:
        point, di = elem
        if di == dir:
            if point.s > news:
                return False
            else:
                newg[newx][newy].remove(elem)
                return True
    
    return True


def search(g, start, end):
    dq = deque([start])
    newg = [[[] for _ in range(len(g[0]))] for _ in range(len(g))]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    distances = []
    while dq:
        point = dq.popleft()

        if point.x == end[0] and point.y == end[1]:
            distances.append(point.s)
        for dir in dirs:
            newx = point.x + dir[0]
            newy = point.y + dir[1]
            news = point.s + 1
            if 0 <= newx < len(g) and 0 <= newy < len(g[0]) and g[newx][newy] != "#" and checkgreater(newx,newy,news,newg,dir):
                if (newx,newy) not in point.v:
                    newvis = point.v.copy()
                    newvis.add((newx,newy))
                    new_point = Point(newx,newy,news,newvis)
                    dq.append(new_point)
                    newg[newx][newy].append((new_point, dir))

    print(distances)
    return max(distances)

grid = open('input.txt','r').read().split('\n')

g = []
su = 0
for row in grid:
    g.append([i for i in row])
    su += sum([1 if i != "#" else 0 for i in row])

print(su)

start = Point(0,1,0, set())

end = (len(grid)-1, len(grid[0])-2)

print(search(g,start,end))






