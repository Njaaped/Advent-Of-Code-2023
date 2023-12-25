

cache = {}


def count(s, crits, reading):
    def countfunction():
        if s == "":
            return 1 if sum(crits) == 0 else 0
        
        if sum(crits) == 0:
            return 0 if "#" in s else 1
        
        if s[0] == "#":
            if reading and crits[0] == 0:
                return 0
            return count(s[1:], (crits[0] - 1, *crits[1:]), True)
        
        if s[0] == ".":
            if reading and crits[0] > 0:
                return 0
            return count(s[1:], crits[1:] if crits[0] == 0 else crits, False)

        if reading:
            if crits[0] == 0:
                return count(s[1:], crits[1:], False)
            return count(s[1:], (crits[0] - 1, *crits[1:]), True)

        return count(s[1:], (crits[0] - 1, *crits[1:]), True) + count(s[1:], crits, False)

    key = hash((s,crits,reading))

    if key not in cache:
        cache[key] = countfunction()


    return cache[key]   

su = 0
l = open('input.txt', 'r').read().split('\n')
co = 0
for s in l:

    newss = s.split()
    criterias = tuple(map(int, newss[1].split(',')))

    st = newss[0] 
    st = '?'.join([st]*5)
    criterias *= 5
    
    su += count(st, criterias, False)
    co += 1
    print(f"{co}/{len(l)}")

print(su)






#finne hvor sum er 3 på rad, det er antall.