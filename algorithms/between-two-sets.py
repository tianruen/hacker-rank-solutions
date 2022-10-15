import math
def getTotalX(a, b):
    gcd = b[0]
    for j in b:
        gcd = math.gcd(gcd,j)
        
    lcm = a[0]
    for i in a:
        lcm = math.lcm(lcm,i)
    
    x = lcm
    count = 0
    while(x<=gcd):
        if gcd%x==0:
            count+=1
        x+=lcm
    
    return count
