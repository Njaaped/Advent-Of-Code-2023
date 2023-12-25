

def ops(letter, curr):
    asc = ord(letter) + curr
    asc *= 17
    return asc % 256

s = open('input.txt','r').read().split(',')


su = 0
d = [[] for _ in range(256)]
focals = {}
for seq in s:
    curr = 0
    
    if "-" in seq:
        op_ind = seq.index("-")
        letters = seq[:op_ind]
        for letter in letters:
            curr = ops(letter, curr)
        if len(d[curr]) < 1:
            continue
        if letters in d[curr]:
            d[curr].remove(letters)

    else:
        op_ind = seq.index("=")
        num = int(seq[op_ind+1:])
        letters = seq[:op_ind]
        for letter in letters:
            curr = ops(letter, curr)
        if letters not in d[curr]:
            d[curr].append(letters)
        focals[letters] = num        

su = 0
for ind, val in enumerate(d,1):
    for i, letters in enumerate(val,1):
        su += (ind)*(i)*(focals[letters])


print(su)

