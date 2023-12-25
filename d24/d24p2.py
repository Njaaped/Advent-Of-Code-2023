import numpy as np

from z3 import Solver, Int

class Line:
    def __init__(self, x, y, z, px, py, pz):
        self.x = x
        self.y = y
        self.z = z
        self.px = px
        self.py = py
        self.pz = pz

# Your file reading code remains the same
file = open('inputtest.txt', 'r').read().splitlines()
lines = []

for line_str in file:
    s = line_str.split(" @ ")
    x, y, z = map(float, s[0].split(', '))
    px, py, pz = map(float, s[1].split(', '))
    lines.append(Line(x, y, z, px, py, pz))


x,y,z,vx,vy,vz = Int('x'),Int('y'),Int('z'),Int('vx'),Int('vy'),Int('vz')
T = [Int(f'T{i}') for i in range(len(lines))]
SOLVE = Solver()
for i, line in enumerate(lines):
  SOLVE.add(x + T[i]*vx - line.x - T[i]*line.px == 0)
  SOLVE.add(y + T[i]*vy - line.y - T[i]*line.py == 0)
  SOLVE.add(z + T[i]*vz - line.z - T[i]*line.pz == 0)

M = SOLVE.model()

print(M.eval(x+y+z))

