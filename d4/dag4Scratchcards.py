lines = open('input4.txt', 'r').read().split('\n')
su = 0
for line in lines:
    i,j = line.index(":")+1,1
    one,two = set(list(map(int, line[i:].split('|')[0].strip().split()))), set(list(map(int, line[i:].split('|')[1].strip().split())))
    su += 0 if len(one.intersection(two)) < 1 else 2**(len(one.intersection(two)) - 1)
print(su)
