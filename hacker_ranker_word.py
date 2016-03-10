'''
Created on Mar 5, 2016

@author: MADHUSUDAN
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=list((raw_input()))
n=(raw_input()).split()
loc =int(n[0])
c = n[1]
s[loc] = c
print reduce(lambda x,y : x+y,s)