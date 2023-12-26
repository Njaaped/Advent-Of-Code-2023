
def recognize_and_predict(pattern):
    new_patterns = [pattern]
    while True:
        new = [pattern[i]-pattern[i-1] for i in range(1,len(pattern))]
        new_patterns.append(new)
        pattern = new
        i = 0
        su = 0
        empty = True
        while i < len(new):
            su += new[i]
            if su != 0:
                empty = False
                break
            i+=1
        if empty:
            break
    
    cur = 0
    rev = new_patterns[::-1]
    for i, pat in enumerate(rev):
        if i == 0:
            continue

        cur = pat[::-1][-1] - cur
        
    return cur

if __name__ == "__main__":
    s = open('d9/input9.txt').read().split('\n')
    su = 0
    for line in s:
        pattern = list(map(int, line.split()))
        su += recognize_and_predict(pattern)
    print(su)
