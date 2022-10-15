def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap = [i for i in apples if s<=i+a<=t]
    og = [j for j in oranges if s<=b+j<=t]
    print(len(ap))
    print(len(og))
