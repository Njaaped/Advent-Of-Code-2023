



def find(instructions, d, startnode):
    current = startnode
    final = "ZZZ"
    counter = 0
    lrmap = {"L":0, "R":1}
    while True:
        instruct = instructions[counter % len(instructions)]
        current = d[current][lrmap[instruct]]
        if current[-1] == "Z":
            break
        counter += 1
    print(counter + 1)
10921547990923

if __name__ == "__main__":
    s = open('input8.txt', 'r').read().split('\n')
    instructions = s[0]
    rest = s[2:]
    d = {}
    nodes = []
    zcount = 0

    for line in rest:
        d[line[:3]] = line[line.index("(")+1:line.index(")")].split(", ")
        if line[2] == "A":
            nodes.append(line[:3])


    print(nodes)
    for node in nodes:
        find(instructions, d, node)



