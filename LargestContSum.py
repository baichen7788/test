# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 20:02:13 2018

@author: USER
"""
# self-written (Not efficient)
def Largest_cont_sum1(a):
    LS=[]
    for i in range(len(a)):
        s=0
        dic={}
        for j in range(i,len(a)):
            s+=a[j]
            dic[s]=[a[i],a[j]]
        LS.append(dic)
    key=max([max(n) for n in LS])
    return key,[d[key] for d in LS if key in d][0]


#Efficient code
def largest_cont_sum(arr):
    if len(arr)==0:
        return 0
    cur_sum=max_sum=arr[0]
    for num in arr[1:]:
        cur_sum=max(cur_sum+num,num)
        max_sum=max(cur_sum,max_sum)
    return max_sum