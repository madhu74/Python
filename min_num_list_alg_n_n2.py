'''
Created on Mar 1, 2016
Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list.
 O(n^2). The second function should be linear O(n).
@author: MADHUSUDAN
'''
from __future__ import print_function
import time
def lst_n2(n):
    min=None
    start_time = time.time()
    for i in n:
        for j in n:
            if min is None:
                min = i
            elif i < j and i < min :
                min = i
            elif j < i and j < min:
                min = j
                
    end_time = time.time()            
    return min,end_time - start_time
#Much more efficient way than my dumb above code
def lst_n22(n):
    min=n[0]
    start_time = time.time()
    for i in n:
        issmall=True
        for j in n:
            if i>j:
                issmall=False
        if issmall:
            min=i  
        end_time = time.time()    
    return min,end_time - start_time
def lst_n(n):
    min = None
    start_time = time.time()
    for i in n:
        if min is None:
            min = i
        if min > i:
            min =i
    end_time = time.time()
    return min, end_time - start_time
#have to tweak this code to perform check as shown in the code
print ("The smallest is %d and the time is %1.10f" %lst_n2([2,3,4,7,5,1,8,6,8,10,50,60,72,32,23,100]))
print ("The smallest is %d and the time is %1.10f" %lst_n([2,3,4,7,5,1,8,6,8,10,50,60,72,32,23,100]))
print ("The smallest is %d and the time is %1.10f" %lst_n22([2,3,4,7,5,1,8,6,8,10,50,60,72,32,23,100]))