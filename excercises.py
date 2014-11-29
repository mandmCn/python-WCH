a = int(raw_input("type in a number"))
n = int(raw_input("type in how many times"))
s = 0

for i in range(1, n+1):
    x = 0
    for k in range(1, i+1):
        x = x + 10**(k-1)*a
    s = s + x
print s
