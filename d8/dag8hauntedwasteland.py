





def find(instructions, d):
    current = "AAA"
    final = "ZZZ"
    counter = 0
    lrmap = {"L":0, "R":1}
    while True:
        instruct = instructions[counter % len(instructions)]
        current = d[current][lrmap[instruct]]
        if current == final:
            break
        counter += 1
    print(counter + 1)





if __name__ == "__main__":
    s = open('d8/input8.txt', 'r').read().split('\n')
    instructions = s[0]
    rest = s[2:]
    d = {}
    for line in rest:
        d[line[:3]] = line[line.index("(")+1:line.index(")")].split(", ")
    find(instructions, d)



