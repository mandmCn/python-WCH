square = []

def comp(x,y):
    x1 = x/100
    x2 = x/10 - 10*x1
    x3 = x - 100*x1 - 10*x2
    y1 = y/100
    y2 = y/10 - 10*y1
    y3 = y - 100*y1 - 10*y2
    if (x1<>y1 and x1<>y2 and x1<>y3 and
        x2<>y1 and x2<>y2 and x2<>y3 and
        x3<>y1 and x3<>y2 and x3<>y3):
        return True
    else:
        return False

for i in range(11,32):
    x = i**2
    x1 = x/100
    x2 = x/10 - 10*x1
    x3 = x - 100*x1 - 10*x2
    if x1<>x2 and x2<>x3 and x1<>x3:
        square.append(x)

for i in square:
    for j in square:
        for k in square:
            if comp(i, j) and comp(i,k) and comp(j,k):
                 print i, j, k

	
