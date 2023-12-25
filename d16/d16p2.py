



from collections import deque
import time 

start = time.time()
s = open('d16/input.txt','r').read().splitlines()


def newshit(next, newx, newy, dir):
    if next == '|':
        if dir == 'u' or dir == 'd':
            return [(newx,newy,dir)]
        return [(newx,newy,'u'), (newx,newy,'d')]
    elif next == '-':
        if dir == "l" or dir == "r":
            return [(newx,newy,dir)]
        return [(newx,newy,'l'), (newx,newy,'r')]
    elif next == "/":
        if dir == "u" or dir == "r":
            return [(newx,newy,'u' if dir == 'r' else 'r')]
        else:
            return [(newx,newy,'d' if dir == 'l' else 'l')]
    elif next == chr(92):
        if dir == 'u' or dir == "l":
            return [(newx,newy,'u' if dir == 'l' else 'l')]
        else:
            return [(newx,newy,'d' if dir == 'r' else 'r')]
    elif next == ".":
        return [(newx,newy,dir)]
    else:
        Exception()

def dothis(startx,starty,dirstart):
    energized = [["." for i in range(len(s[0]))] for j in range(len(s))]
    energized[startx][starty] = "#"
    dq = deque()
    beenthere = set()
    next = s[startx][starty]
    for elem in newshit(next,startx,starty,dirstart):
        dq.append(elem)
        beenthere.add(elem)
        energized[startx][starty] = "#"
    # r l u d

    dirmap={
        'r':(0,1),
        'l':(0,-1),
        'u':(-1,0),
        'd':(1,0)
    }

    # dirs = {'l':'<','r':'>','d':'v','u':'^'}
    #nums = {'2','3','4'}

    while dq:
        x,y,dir = dq.pop()
        

        newx,newy = x+dirmap[dir][0],y+dirmap[dir][1]


        if 0 > newx or newx >= len(s) or 0 > newy or newy >= len(s[0]):
            continue
        
        next = s[newx][newy]

        for elem in newshit(next,newx,newy,dir):
            if elem not in beenthere:
                dq.append(elem)
                beenthere.add(elem)
                energized[newx][newy] = "#"
        

    su = 0
    for line in energized:
        for c in line:
            if c == "#":
                su += 1
    return su




maxsu = 0
for i in range(len(s)):
    su = dothis(i,0,'r')

    if su > maxsu:
        maxsu = su
    su = dothis(i,len(s[0])-1,'l')

    if su > maxsu:
        maxsu = su

for j in range(len(s[0])):
    su = dothis(0,i,'d')

    if su > maxsu:
        maxsu= su
    su = dothis(len(s)-1,i,'u')

    if su > maxsu:
        maxsu = su

print(maxsu)

print(time.time()-start)





