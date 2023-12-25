


class Line:
    def __init__(self,x,y,px,py):
        self.x = x
        self.y = y
        self.px = px
        self.py = py
        self._create_slope()
    
    def _create_slope(self):
        self.m = ((self.py+self.y) - self.y)/((self.px + self.x) - self.x)
        self.b = self.y - self.m * self.x


    def calulate_interception(self, other):
        if self.m == other.m and other.b != self.b:
            return None
        
        x = (other.b - self.b) / (self.m - other.m)
        y = x*self.m + self.b

        if self.px > 0:
            if other.px > 0:
                if x >= max(self.x,other.x):
                    return (x,y)
                return None
            else:
                if x >= self.x and x <= other.x:
                    return (x,y)
                return None
        else:
            if other.px > 0:
                if x <= self.x and x >= other.x:
                    return (x,y)
                return None
            else:
                if x <= self.x and x <= other.x:
                    return (x,y)
                return None


file = open('input.txt','r').read().splitlines()
lines = []
for line in file:
    s = line.split(" @ ")

    x,y,_ = map(float, s[0].split(', '))
    px,py,_ = map(float, s[1].split(', '))

    lines.append(Line(x,y,px,py))


su = 0
for r, row in enumerate(lines):
    for col in lines[:r]:
        intercept = row.calulate_interception(col)
        if intercept != None:
            x,y = intercept
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                su += 1
               
     

print(su)


