import datetime

count = 0
for y in range(2014,2025):
    for m in range(1,13):
        day = datetime.date(y,m,13)
	if day.weekday() == 4:
	    print day
	    count = count+1
print count
