lane = []
for i in range(100):
    i = False
    lane.append(i)

for s in range(100):
    for k in range(100):
        if (k+1)%(s+1) == 0:
            lane[k] = not lane[k]

for i in range(100):
    if lane[i]:
	print i + 1, "is on."
        
    

