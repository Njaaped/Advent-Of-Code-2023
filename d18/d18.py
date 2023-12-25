



grid = [["." for _ in range(500)] for __ in range(500)]

current = (len(grid) // 2, len(grid[0]) // 2)
grid[current[0]][current[1]] = "#"

s = open("d18/input.txt",'r').read().splitlines()


def bucket_fill(grid, row, col):
    stack = [(row, col)]

    while stack:
        r, c = stack.pop()

        if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == ".":
            grid[r][c] = "#"

            stack.append((r + 1, c))
            stack.append((r - 1, c))
            stack.append((r, c + 1))
            stack.append((r, c - 1))

dir = {
    "R":(0,1),
    "L":(0,-1),
    "U":(-1,0),
    "D":(1,0)
}

i = 0
for line in s:
    newline = line.split()
    d = newline[0]
    amount = int(newline[1])
    for _ in range(amount):
        current = (current[0] + dir[d][0], current[1] + dir[d][1])
        print(current)
        grid[current[0]][current[1]] = "#"
        i += 1


bucket_fill(grid, 130, 300)


i = 0
for line in grid:
    for ch in line:
        if ch == "#":
            i += 1



print(i)


file = open("d18/d18drawing.txt",'w')
file.write("lollol")
for line in grid:
    file.write(''.join(i for i in line) + "\n")




