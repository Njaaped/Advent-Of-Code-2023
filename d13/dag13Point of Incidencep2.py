



def isvertical(pattern, index):

    p1 = pattern[:index][::-1]
    p2 = pattern[index:]
    i = 0
   
    while i < min(len(p2), len(p1)):
        if p1[i] == p2[i]:
            i += 1
            continue
        else:
            return False
        

    return True


def checkpattern(pattern, last):
    
    for i in range(1, len(pattern)):
        if i * 100 != last:
            if isvertical(pattern, i):
        
                return i*100
        
    trans = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]

    for i in range(1, len(trans)):
        if i != last:
            if isvertical(trans, i):
                return i
    
    return None

def checkpattern2(pattern):

    oldsu = checkpattern(pattern, None)

    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == ".":
                pattern[i][j] = "#"
                su = checkpattern(pattern, oldsu)
                if su != None and su != oldsu:
                    return su
                if su == oldsu:
                    su = None
                pattern[i][j] = "."
            else:
                pattern[i][j] = "."
                su = checkpattern(pattern, oldsu)
                if su != None and su != oldsu:
                    return su
                if su == oldsu:
                    su = None
                pattern[i][j] = "#"

    return 0

s = open('input.txt', 'r').read().split('\n')

pattern = []
su = 0

for line in s:
    if line == "":
        su += checkpattern2(pattern)
        pattern = []
        continue

    pattern.append([i for i in line])


su += checkpattern2(pattern)

print(su)