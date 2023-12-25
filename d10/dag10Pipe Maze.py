
from collections import deque



#"┌ ┐ └ ┘"

def c(letter):
    d = {
        "L" : '└',
        "J" : '┘',
        "7" : "┐",
        "F" : "┌",
    }

def findpath(adj, spos):

    rows = len(adj)
    cols = len(adj[0])

    legal = {
        "|" : set(['south', 'north']),
        "-" : set(['east', 'west']),
        "L" : set(['north', 'east']),
        "J" : set(['north', 'west']),
        "7" : set(['south', 'west']),
        "F" : set(['east', 'south'])
    }

    new = {
        "|" : {'south': 'north', 'north': 'south'},
        "-" : {'east': 'west', 'west': 'east'},
        "L" : {'north': 'east', 'east': 'north'},
        "J" : {'north': 'west', 'west': 'north'},
        "7" : {'south': 'west', 'west': 'south'},
        "F" : {'east': 'south', 'south': 'east'},
    }

    dirmap = {
        'north' : 'south',
        'west' : 'east',
        'south' : 'north',
        'east' : 'west'
    }

    nextdir = {
        'north' : (1, 0),
        'south' : (-1, 0),
        'west' : (0, 1),
        'east' : (0, -1)
    }


    visited = set()
    visited.add(spos)

    dq = deque()

    dq.append((spos[0], spos[1], 0, -1))
    #edgecase
    x, y, dist, nodedir = dq.popleft()


    for key, val in nextdir.items():
        newx = x + val[0]
        newy = y + val[1]
        if 0 <= newx < rows and 0 <= newy < cols and adj[newx][newy] in legal:
            s = adj[newx][newy]
            
            if key in legal[s]:
                newnodedir = new[s][key]
                newdist = dist + 1
                dq.append((newx,newy,newdist,newnodedir))
                visited.add((newx,newy))
    
    maksdist = 0


    while dq:
        x, y, dist, nodedir = dq.popleft()
        otherdir = dirmap[nodedir]
        newx = x + nextdir[otherdir][0]
        newy = y + nextdir[otherdir][1]

        if 0 <= newx < rows and 0 <= newy < cols and adj[newx][newy] in legal and (newx,newy) not in visited:
            s = adj[newx][newy]

            if otherdir in legal[s]:
                newnodedir = new[s][otherdir]
                newdist = dist + 1
                dq.append((newx,newy,newdist,newnodedir))
                visited.add((newx,newy))
                if newdist > maksdist:
                    maksdist += 1
    
    print(maksdist)


if __name__ == "__main__":
    s = open('input10.txt').read().split('\n')
    adj = []
    finds = (False, None)

    for ind, line in enumerate(s):
        adj.append([i for i in line])
        if not finds[0] and "S" in line:
            for newind, elem in enumerate(line):
                if elem == "S":
                    finds = (True, (ind, newind))
    findpath(adj, finds[1])
    

