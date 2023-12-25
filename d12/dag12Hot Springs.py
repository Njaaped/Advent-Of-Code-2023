import math
from itertools import product

def generate_binary_numbers(n):
    return list(product([0, 1], repeat=n))

def suinrow(binarr, criterias):

    count = 0
    for i in range(len(binarr)):
        su = 0
        currcrit = 0
        crit = criterias[currcrit]
        for ind, num in enumerate(binarr[i]):
            if num == 1:
                su += num
            elif crit > su > 0 and num == 0:
         
                break
                #su = 0
            if su == crit:
                if ind + 1 < len(binarr[i]) and binarr[i][ind+1] != 1:
                    currcrit += 1
                    if currcrit < len(criterias):
                        crit = criterias[currcrit]
                        su = 0
                    else:
                        if sum(binarr[i][ind+1:]) == 0:
                            count += 1
                    
     
                        break
                elif ind + 1 == len(binarr[i]) and currcrit == len(criterias) - 1:
                    count += 1
       
            elif su > crit:
                break

    return(count)

count = 0
su = 0
l = open('input.txt', 'r').read().split('\n')
d = {}
for s in l:
    newss = s.split()
    criterias = list(map(int, newss[1].split(',')))
    st = newss[0]
    sucrit = sum(criterias)
    if (len(st), sucrit) not in d:
        binarr = generate_binary_numbers(len(st))
        d[(len(st), sucrit)] = [row for row in binarr if sum(row) == sucrit]

    bincop = d[(len(st), sucrit)]
    i = 0
    while i < len(bincop[0]):
        bicopcop = []
        for bi in bincop:
            if st[i] == "#" and bi[i] == 1:
                bicopcop.append(bi)
            elif st[i] == "#" and bi[i] == 0:
                continue
            elif st[i] == "." and bi[i] == 0:
                bicopcop.append(bi)
            elif st[i] == "." and bi[i] == 1:
                continue
            elif st[i] == "?":
                bicopcop.append(bi)
                
        bincop = bicopcop
        i += 1

                
    nu = suinrow(bincop, criterias)
    su += nu
    count += 1
    print(f'{count}/{len(l)}')

print(su)






#finne hvor sum er 3 på rad, det er antall.