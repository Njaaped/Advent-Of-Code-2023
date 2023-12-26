

def getddistances(distancestring) -> list:
    colon = distancestring.index(":")
    li = list(map(int, distancestring[colon+1:].strip().split()))

    return li

def gettimes(timestring) -> list:
    colon = timestring.index(":")
    li = list(map(int, timestring[colon+1:].strip().split()))
    return li

def task(distancestring, timestring):
    distances = getddistances(distancestring)
    times = gettimes(timestring)
    stores = [[] for _ in range(len(times))]
    ind = 0

    for distance, time in zip(distances, times):
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
                stores[ind].append(current)
        ind += 1
    su = 1
    print(stores)
    for l in stores:
        su *= len(l)
    
    print(su)


if __name__ == "__main__":
    s = open('d6/input6.txt','r').read().split("\n")
    task(s[1],s[0])






