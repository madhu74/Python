'''
Created on Mar 16, 2016

@author: MADHUSUDAN
'''
import re
file_name =raw_input("File Name:")
k=list()
j=list()
file_name
#"regex_sum_42.txt,regex_sum_248180.txt"
handle=open(file_name)
for line in handle:
    line=line.rstrip()
    k=re.findall('[0-9]+', line)
    for i in k:
        j.append(int(i))
        
#j=[int(x) for x in j]
print"THere are %d values with the sum= %d"%(len(j),sum(j))
