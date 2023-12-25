from collections import defaultdict
import sys
from decimal import Decimal

def ismapped(map, seed):
    li = list(map.keys())

    for ind in range(0,len(li)):
        if li[ind] <= seed < li[ind] + map[li[ind]][1]:
            return seed + (map[li[ind]][0] - li[ind])
        
    return seed

lines = open('input5.txt','r').read().split('\n')

d = {}
seeds = []

last = ""
for line in lines:
    if line == '':
        continue
    if line[0].isnumeric():
        newline = tuple(map(Decimal, line.strip().split()))
        d[last][newline[1]] = (newline[0], newline[2])
        continue

    ind = line.index(":")
    word = line[:ind]
    if word == 'seeds':
        seeds = list(map(Decimal, line[ind+1:].strip().split()))
        continue
    if last != '':
        d[last] = dict(sorted(d[last].items(), key=lambda x: x[0]))

    d[word] = {}
    last = word

smallest = sys.maxsize
count = 0
while seeds:
    seed = seeds.pop()
    for key, val in d.items():
        seed = ismapped(val, seed)
  
    if seed < smallest:
        smallest = seed



print(smallest)


