

file = open('d2/input.txt','r').read().splitlines()

boundries = {
    'red':12,
    'green':13,
    'blue':14,
}

loc = {
    'red':0,
    'green':1,
    'blue':2,
}

su = 0
for line in file:
    game, rest = line.split(':')
    gamenum = int(game.split()[1])
    rest = rest.strip().split(';')
    t = True
    for elem in rest:
        new = elem.split(", ")
        counters = [0,0,0]
        for item in new:
            num, color = item.split()
            counters[loc[color]] += int(num)
        if not all([True if j <= boundries[list(boundries.keys())[i]] else False for i, j in enumerate(counters)]):
            t = False
            break
    if t:
        su += gamenum

print(su)




