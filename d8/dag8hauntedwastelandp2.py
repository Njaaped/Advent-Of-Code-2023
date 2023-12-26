
import math


def find(instructions, d, startnode):
    current = startnode
    counter = 0
    lrmap = {"L":0, "R":1}
    while True:
        instruct = instructions[counter % len(instructions)]
        current = d[current][lrmap[instruct]]
        if current[-1] == "Z":
            break
        counter += 1
    return counter + 1

if __name__ == "__main__":
    s = open('d8/input8.txt', 'r').read().split('\n')
    instructions = s[0]
    rest = s[2:]
    d = {}
    nodes = []
    zcount = 0

    for line in rest:
        d[line[:3]] = line[line.index("(")+1:line.index(")")].split(", ")
        if line[2] == "A":
            nodes.append(line[:3])


    res = []
    for node in nodes:
        res.append(find(instructions, d, node))

    print(math.lcm(*res))

