
# Take out 1 number from arr1 and it becomes new arr2.
#Find out the number taken out

def finder1(arr1,arr2):
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    
    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr1[-1]



# Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. 
#The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet). 
#To create such a "default" item, it calls the function object that you pass in the constructor (more precisely, 
#it's an arbitrary "callable" object, which includes function and type objects). 
#defaultdict(int) create dict with default item of int = 0
import collections
def finder2(arr1,arr2):
    d=collections.defaultdict(int)
    
    for num in arr2:
        d[num] += 1
        
    for num in arr1:
        
        if d[num] == 0:
            return num
        else:
            d[num] -=1 
            

# Make use of XOR ( Hard to understand)
def finder3(arr1,arr2):
    result=0
    #perform XOR between the number and array
    for num in arr1+arr2:
        result ^= num
        print result
    return result