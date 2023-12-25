



#start at 0
#ascii code, curr + ascii
# current value *= 17
# remainder 256 so % 256


def ops(letter, curr):
    asc = ord(letter) + curr
    asc *= 17
    return asc % 256

s = open('inputtest.txt','r').read().split(',')


su = 0
for seq in s:
    curr = 0
    for letter in seq:
        curr = ops(letter, curr)
    su += curr

print(su)

