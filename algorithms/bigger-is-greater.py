def biggerIsGreater(w):
    original = w
    w = list(w)
    i = len(w)-1
    
    while i > 0:
        if w[i]>w[i-1]:
            j = len(w)-1
            while j > 0:
                if w[j]>w[i-1]:
                    w[j],w[i-1]=w[i-1],w[j]
                    break
                else:
                    j-=1
            break        
        else:
            i-=1
            
    w = ''.join(w)
    if w == original:
        return 'no answer'
    else:    
        w_front = w[:i]
        w_back = ''.join(sorted(w[i:]))
        return w_front+w_back
