#!/usr/bin/env python3
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
combined=zip(l1,l2)
    
ans=[]
def filters(x):
    a,b = x
    if len(a)>3 and len(b)>3:
        return a,b

opposites=filter(filters,combined)
print(list(opposites))