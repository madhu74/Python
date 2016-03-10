'''
Created on Mar 1, 2016

@author: MADHUSUDAN
'''
from __future__ import print_function
import time
def sum_to_n(n):
    start = time.time()
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    end = time.time()
    return sum,end-start

print  ("Sum is %d and time is %10.9f"% sum_to_n(10000))
