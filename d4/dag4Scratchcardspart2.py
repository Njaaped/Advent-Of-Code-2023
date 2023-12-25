lines = open('input4.txt', 'r').read().split('\n')
d = {i:1 for i in range(1,len(lines)+1)}
for line in lines:
    i = line.index(":") + 1
    num = int(line[5:line.index(":")])
    one, two = set(list(map(int, line[i:].split('|')[0].strip().split()))), set(list(map(int, line[i:].split('|')[1].strip().split()))) 
    for i in range(1, len(one.intersection(two)) + 1):
        d[num + i] += d[num]
print(sum(d.values()))