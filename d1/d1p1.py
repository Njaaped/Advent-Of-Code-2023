

file = open('d1/input.txt','r').read().splitlines()


def findnum(line):
    arr = [i for i in line if i.isnumeric()]
    return arr[0]+arr[-1]

su = 0
for line in file:
    su += int(findnum(line))
print(su)
