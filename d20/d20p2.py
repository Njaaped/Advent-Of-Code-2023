

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


doubles = []
doublesset = set()

for name, mod in d.items():
    for item in mod.destination_modules:
        if item in d and d[item].prefix == "&":
            d[item].memory[name] = mod.memory
            if mod.prefix == "&" and d[item].modulename == "dn":
                doubles.append(name)
                doublesset.add(name)

lo = hi = 0
count = 1
rxlowfind = False

counter = {}
for elem in doubles:
    counter[elem] = 0

for mem in d["dd"].memory:
    for mem2 in d[mem].memory:
        print(d[mem2].prefix)

print(d["dd"].memory)

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

        if mod.prefix == "%":
            if pulse == "lo":
                mod.memory = "on" if mod.memory == "off" else "off"
                pulse = "hi" if mod.memory == "on" else "lo"
                for elem in mod.destination_modules:
                    q.append((target, elem, pulse))
        else:
            mod.memory[origin] = pulse
            pulse = "lo" if all(x == "hi" for x in mod.memory.values()) else "hi"
            if target in doublesset and pulse == "hi":
                print(target, count)
            for elem in mod.destination_modules:
                q.append((target, elem, pulse))
        

    count += 1
