'''
Created on Feb 11, 2016

@author: MADHUSUDAN
'''

'''test code'''

d={}
'''for i in range(int(raw_input())):
    line=raw_input().split()
    d[line[0]]=sum(map(float,line[1:]))/3

print '%.2f' % d[raw_input()]
'''
'''for printing certain pattern.
from __future__ import print_function
map(lambda x: print(x,end=''), range(1,input()+1))
print "madhu "*10 '''

'''X = int(raw_input())
Y = int(raw_input())
Z = int(raw_input())
N = int(raw_input())
A = []
[ A.append([i,j,k]) for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k != N ]
print (A)'''
k=[]
[k.append([i,j]) for i in range(1,10) for j in range(1,10)]
print k
