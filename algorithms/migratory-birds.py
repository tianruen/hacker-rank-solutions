def migratoryBirds(arr):
    unique = set(arr)
    x = 1
    for i in unique:
        if arr.count(i)>arr.count(x):
            x = i
        elif arr.count(i)==arr.count(x) and i < x:
            x = i
            
    return x
