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


energized = [["." for i in range(len(s[0]))] for j in range(len(s))]
energized[0][0] = "#"
dq = deque()

drawing2 = [["." for i in range(len(s[0]))] for j in range(len(s))]

beenthere = set()


next = s[0][0]
for elem in newshit(next,0,0,'r'):
    dq.append(elem)
    beenthere.add(elem)
# r l u d

dirmap={
    'r':(0,1),
    'l':(0,-1),
    'u':(-1,0),
    'd':(1,0)
}

dirs = {'l':'<','r':'>','d':'v','u':'^'}
nums = {'2','3','4'}

while dq:
    x,y,dir = dq.pop()
    
    energized[x][y] = "#"
    
    if drawing2[x][y] in dirs.values():
        drawing2[x][y] = '2'
    elif drawing2[x][y] in nums:
        drawing2[x][y] = str(int(drawing2[x][y]) + 1)
    else:
        drawing2[x][y] = dirs[dir]


    newx,newy = x+dirmap[dir][0],y+dirmap[dir][1]


    if 0 > newx or newx >= len(s) or 0 > newy or newy >= len(s[0]):
        continue
    
    next = s[newx][newy]

    for elem in newshit(next,newx,newy,dir):
        if elem not in beenthere:
            dq.append(elem)
            beenthere.add(elem)
    

# writefile = open('d16drawing.txt','w')

# su = 0
# for line in energized:
#     for c in line:
#         if c == "#":
#             su += 1
#     writefile.write(''.join(i for i in line)+'\n')


# writefile2 = open('d16drawing2.txt','w')
# for line in drawing2:
#     writefile2.write(''.join(i for i in line)+'\n')


print(su)
print(time.time()-start)


