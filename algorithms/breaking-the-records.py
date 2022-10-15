def breakingRecords(scores):
    minscore = scores[0]
    maxscore = scores[0]
    x = 0 #number of times break maximum scoring record
    y = 0 #number of times break minimum scoring record
    
    for i in scores:
        if i > maxscore:
            x+=1
            maxscore = i
        elif i < minscore:
            y+=1
            minscore = i
    
    return (x,y) 
