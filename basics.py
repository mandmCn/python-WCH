n = int(raw_input("enter n(1<=n<=20)"))
k = int(raw_input("enter k(1<=k<=5)"))
number = 0
nk = n**k

for i in range(1,nk + 1):
    if nk%i == 0:
        number = number + i

print number
    