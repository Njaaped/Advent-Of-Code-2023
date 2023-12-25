

def getddistances(distancestring) -> int:
    colon = distancestring.index(":")
    li = int(distancestring[colon+1:].replace(" ", ""))
    return li

def gettimes(timestring) -> int:
    colon = timestring.index(":")
    li = int(timestring[colon+1:].replace(" ", ""))
    return li

def task(distancestring, timestring):
    distance = getddistances(distancestring)
    time = gettimes(timestring)
    stores = []

    minspeed = distance / time
    i = int(minspeed)
    peaked = False
    last = -1
    while True:

        if i > time:
            break

        timeleft = time - i 
        current = timeleft*i

        if current < last:
            peaked = True

        if peaked and current < distance:
            break
        
        last = current
        i+=1
        if current > distance:
            stores.append(current)
 
    print(len(stores))


if __name__ == "__main__":
    s = open('input6.txt','r').read().split("\n")
    task(s[1],s[0])


