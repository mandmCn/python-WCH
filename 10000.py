import datetime

d1 = datetime.date(2001,10,3)
d = datetime.timedelta(days=10000)
d2 = d1 + d

print d2
print d2.weekday()
