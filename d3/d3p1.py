

import re

file = open('d3/input.txt','r').read().splitlines()

def getnumpos(line, lineindex, nums):
    pattern = re.compile(r'\d+')
    numbers = [(match.start(), match.group())for match in pattern.finditer(line)]
    for start, num in numbers:
        pos = (lineindex, start - 1, int(num))
        nums.append(pos)
    return nums

nums = []
grid = []
for i, line in enumerate(file):
    getnumpos(line, i, nums)  
    grid.append(list(line))


dirs = [-1,0,1]
su = 0

symbols = set()

for elem in nums:
    x,y,num = elem
    for i in range(len(str(num))+2):
        for dir in dirs:
            dx = dir
            dy = i
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and not grid[x+dx][y+dy] == '.' and not grid[x+dx][y+dy].isnumeric():
                su += int(num)
                symbols.add(grid[x+dx][y+dy])
                break
        else:
            continue
        break

print(su)




