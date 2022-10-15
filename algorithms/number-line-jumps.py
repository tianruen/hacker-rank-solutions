def kangaroo(x1, v1, x2, v2):
    # Note that x2 > x1
    a = x2 - x1
    b = v1 - v2
    
    if b>0 and a%b ==0:
        return 'YES'
    else:
        return 'NO'
