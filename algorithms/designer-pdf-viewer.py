def designerPdfViewer(h, word):
    a = ('abcdefghijklmnopqrstuvwxyz')
    d = dict(zip(a,h))
    x = []
    for i in word:
        x.append(d[i])
    
    return len(word)*max(x)
