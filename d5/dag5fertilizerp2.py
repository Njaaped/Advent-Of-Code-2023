
lines = open('input5.txt','r').read().split('\n')

d = []
seeds = []

last = ""
for line in lines:
    if line == '':
        continue
    if line[0].isnumeric():
        newline = tuple(map(int, line.strip().split()))
        d[-1].append((newline[0], newline[1], newline[2]))
        continue
    ind = line.index(":")
    word = line[:ind]
    if word == 'seeds':
        seeds_pairs = list(map(int, line[ind+1:].strip().split()))
        continue
    d.append([])

def rangeshit(start, end, d):
    seeds = [(start, end)]
    for m in d:
        newseeds = []
        while len(seeds) > 0:
            s,e = seeds.pop()
            for a,b,c in m:
                overlapstart = max(s,b)
                overlapend = min(e, b+c)            
                if overlapstart < overlapend:
                    newseeds.append((overlapstart - b + a, overlapend - b + a))
                    if overlapstart > s:
                        seeds.append((s, overlapstart))
                    if e > overlapend:
                        #print("overlap:", overlapend, e)
                        seeds.append((overlapend, e))
                    break
            else:
                newseeds.append((s,e))
        
        seeds[:] = newseeds

    return min(seeds)[0]

ans = []

for i in range(1,len(seeds_pairs),2):
    ans.append(rangeshit(seeds_pairs[i-1], seeds_pairs[i-1] + seeds_pairs[i], d))

print(min(ans))