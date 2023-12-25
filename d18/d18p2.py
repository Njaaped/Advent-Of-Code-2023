from dataclasses import dataclass

def hextonum(hexcode):
    return int(hexcode[2:-2], 16)

@dataclass
class Point:
    x:int
    y:int

boundary = 0
points = [Point(0,0)]
ypos = 0
xpos = 0
s = open("input.txt",'r').read().split("\n")
for line in s:
    newline = line.split()
    dir = int(newline[2][-2])
    amount = hextonum(newline[2])
    if dir == 3:
        ypos -= amount
    elif dir == 1:
        ypos += amount
    elif dir == 0:
        xpos += amount
    elif dir == 2:
        xpos -= amount

    boundary += amount
    points.append(Point(xpos,ypos))


print(points)
su = 0
for i in range(len(points) - 1):
    su += (points[i].x * (points[i-1].y - points[i+1].y))

su += (points[len(points)-1].x * (points[len(points)-2].y - points[0].y))

su = abs(su / 2)

print(boundary)

inside = su - boundary // 2 + 1

print(inside + boundary)