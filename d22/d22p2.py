
from collections import defaultdict,deque


s = open('input.txt','r').read().split('\n')


class brick:
    def __init__(self,x,y,z,a,b,c) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c
        self.cords = self.setcords()

    def setcords(self):
        arr1 = [self.x, self.y, self.z]
        arr2 = [self.a, self.b, self.c]
        diff = [abs(e1 - e2) for e1, e2 in zip(arr1, arr2)]
        result = set()

        if sum(diff) == 0:
            return [tuple(arr1)]

        for i, elem in enumerate(diff):
            if elem != 0:
                for e in range(min(arr1[i], arr2[i]),min(arr1[i], arr2[i]) + elem + 1):
                    newarr = arr1.copy()
                    newarr[i] = e
                    result.add(tuple(newarr))
        
        return result
    
    def getnewcords(self):
        li = []
        for elem in self.cords:
            newelem = tuple(x+y for x,y in zip(elem,(0,0,-1)))
            li.append(newelem)
        return li
    
    def setnewcords(self, li):
        self.cords = set(li)
        self.z -= 1
        self.c -= 1

    def __lt__(self, other) -> bool:
        return min(self.z, self.c) < min(other.z, other.c)
    
    def __str__(self):
        return f"Brick(x={self.x}, y={self.y}, z={self.z}, a={self.a}, b={self.b}, c={self.c})"

    def overlaps(self, other):
        return max(self.x,other.x) <= min(self.a,other.a) and max(self.y, other.y) <= min(self.b,other.b)

bricks = []


for line in s:
    li = line.split('~')
    x,y,z = map(int, li[0].split(','))
    a,b,c = map(int, li[1].split(','))

    bricks.append(brick(x,y,z,a,b,c))

bricks.sort()

newall = set()

levels = defaultdict(list)
every = []

for br in bricks:
    
    breaking = False

    while True:
        new = br.getnewcords()
        for elem in new:
            if elem in newall:
                breaking = True
            if elem[2] < 1:
                breaking = True

        if breaking:
            break
        
        br.setnewcords(new)

    every.append(br)

    newall.update(br.cords)

k_supports_v = {i: set() for i in range(len(every))}
v_supports_k = {i: set() for i in range(len(every))}

for j, br1 in enumerate(every):
    for i,br2 in enumerate(every[:j]):
        if br1.overlaps(br2) and br1.z == br2.c + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total = 0

for i in range(len(bricks)):
    q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(q)
    falling.add(i)
    
    while q:
        j = q.popleft()
        for k in k_supports_v[j] - falling:
            if v_supports_k[k] <= falling:
                q.append(k)
                falling.add(k)
    
    total += len(falling) - 1

print(total)

