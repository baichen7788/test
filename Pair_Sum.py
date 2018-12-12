# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:42:35 2018

@author: USER
"""

#pair sum
def pair_sum(arr,k):
    if len(arr) < 2:
        return
    
    #Set for tracking
    seen=set()
    output=set()
    
    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
            
    return output


pair_sum([1,3,5,2,6,7,4],10)