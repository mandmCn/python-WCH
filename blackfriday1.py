count = 0
for x in range(1,10):
    for y in range(1,x+1):
        z = int((10*x + y - 10*y - x)**0.5)
        if z**2 == 10*x + y - 10*y - x:
            print 10*x + y
            count = count+1
print count
