def sanitizelist(l, i=0):
    if i>=len(l):
        return l
    elif l[i] < 0:
        l[i]=0
    return sanitizelist(l, i+1)
    
print("sanitized list is: ", sanitizelist([5,-1,9,-7,4,-3,2]))
