#!/usr/bin/env python
# coding: utf-8

# In[1]:


def climbingLeaderboard(ranked, player):
    r = []
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    
    for score in player:
        start = 0
        end = len(ranked) - 1
        middle = (start+end)//2
        while start<=end:
            if score>ranked[middle]:
                end = middle - 1
            elif score<ranked[middle]:
                start = middle + 1
            else:
                start=middle
                break
            middle = (start+end)//2
        r.append(start+1)
    return r

