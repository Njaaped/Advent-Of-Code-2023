

file = open('d2/input.txt','r').read().splitlines()


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
    largest = [1,1,1]
    for elem in rest:
        new = elem.split(", ")
        counters = [0,0,0]
        for item in new:
            num, color = item.split()
            counters[loc[color]] += int(num)
        for i, count in enumerate(counters):
            if count > largest[i]:
                largest[i] = count
    if t:
        su += largest[0] * largest[1] * largest[2]

print(su)




