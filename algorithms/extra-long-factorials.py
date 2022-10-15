def extraLongFactorials(n):
    a = 1
    while n>0:
        a*=n
        n-=1
    print(a)
