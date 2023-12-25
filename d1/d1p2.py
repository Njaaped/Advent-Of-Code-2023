




file = open('d1/input.txt','r').read().splitlines()

d = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}


def findnum(line):
    i = 0
    arr = []
    while i < len(line):
        for key, value in d.items():
            if line[i:i+len(key)] == key:
                arr.append(str(value))
                i += 1
                break
        else:
            if line[i].isnumeric():
                arr.append(line[i])
            i += 1
    
    return arr[0]+arr[-1]
 

su = 0
for line in file:
    su += int(findnum(line))
print(su)

