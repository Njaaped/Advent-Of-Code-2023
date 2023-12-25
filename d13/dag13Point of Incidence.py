



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


def checkpattern(pattern):
    
    for i in range(1, len(pattern)):
        if isvertical(pattern, i):
            return i*100
    
    trans = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]

    for i in range(1, len(trans)):
        if isvertical(trans, i):
            return i



s = open('input.txt', 'r').read().split('\n')

pattern = []
su = 0

for line in s:
    if line == "":
        su += checkpattern(pattern)
        pattern = []
        continue

    pattern.append([i for i in line])

su += checkpattern(pattern)

print(su)