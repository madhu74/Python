'''
Created on Mar 24, 2016

@author: MADHUSUDAN
'''
# Uses python2
n = int(raw_input())
a = [int(x) for x in raw_input().split()]
try:
    assert(len(a) == n)
except:
    print 'check the input'
    exit()

result = 0

for i in xrange(0, n):
    for j in xrange(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]

print(result)
