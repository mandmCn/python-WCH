def is_prime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i == 0:
            return False
    return True
    
factors = []
n = int(raw_input("Enter a number:"))
i = n
new = n

while new > 1:
    if(new%i == 0) and is_prime(i):
        new = new/i
        factors.append(i)
    else:
        i = i-1
        
print factors
    
