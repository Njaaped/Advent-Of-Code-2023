

from dataclasses import dataclass
from collections import deque

@dataclass
class Module:
    modulename: str
    prefix: str
    destination_modules: list
    def __post_init__(self):
        self.memory = {} if self.prefix == "&" else "off"

    

s = open('input.txt','r').read().split('\n')

d = {

}

for line in s:
    name_prefix, rest = line.split(" -> ")

    dest = rest.split(", ")

    if name_prefix == "broadcaster":
        broadcasting = dest
    else:
        prefix = name_prefix[0]
        name = name_prefix[1:]
        d[name] = Module(name, prefix, dest)

for name, mod in d.items():
    if mod.prefix == "%":
        for item in mod.destination_modules:
            if d[item].prefix == "&":
                d[item].memory[name] = mod.memory

lo = hi = 0


count = 0
rxlowfind = False

print(d["dn"].memory)

while True:
    lo += 1
    q = deque()
    for name in broadcasting:
        q.append(("broadcasting", name, "lo"))
    while q:
        origin, target, pulse = q.popleft()

        if pulse == "lo":
            lo += 1
        else:
            hi += 1

        if target not in d:
            continue

        mod = d[target]

        if target == "dn":
            rxlowfind = True
            break

        if mod.prefix == "%":
            if pulse == "lo":
                mod.memory = "on" if mod.memory == "off" else "off"
                pulse = "hi" if mod.memory == "on" else "lo"
                for elem in mod.destination_modules:
                    q.append((target, elem, pulse))
        else:
            mod.memory[origin] = pulse
            pulse = "lo" if all(x == "hi" for x in mod.memory.values()) else "hi"
            for elem in mod.destination_modules:
                q.append((target, elem, pulse))

    count += 1
    print(count)
    if rxlowfind == True:
        break


print(count)
print(hi*lo)
