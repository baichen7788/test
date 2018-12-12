# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:39:09 2018

@author: USER
"""

#Check if two strings have same letters
def anagram1(a,b):
    a=a.replace(' ','').lower()
    b=b.replace(' ','').lower()
    return sorted(a) == sorted(b)

def anagram2(s1,s2):
    s1=s1.replace(' ','').lower()
    s2=s2.replace(' ','').lower()
    
    count={}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter]=1
            
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter]=1
            
    for k in count:
        if count[k] != 0:
            return False
    return True