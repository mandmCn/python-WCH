for a in range (1,9):
    for b in range (0,9):
        if (int((1100*a + 11*b)**0.5))**2 == 1100*a + 11*b:
            print 1100*a + 11*b
