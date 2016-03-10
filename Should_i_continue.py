N = int(raw_input())
l=[]
low= None
s_low = None
for i in range(0,N):
    name = raw_input()
    grade = float(raw_input())
    l.append([name,grade])
for sl in l:
    if low is None:
        low =  sl[1]
        #s_low = sl[1]
    elif s_low is None:
        s_low = sl[1]
    if low >= sl[1]:
        s_low,low =  low,sl[1]
    elif sl[1]  < s_low and low  < sl[1] :
        s_low = sl[1]
#print s_low,low
l.sort()
for sl in l:
    if sl[1] == s_low:
        print sl[0]
        
        '''Or the fucking code below, to print the second lowers number'''
        
        a = [[raw_input(), float(raw_input())] for i in xrange(int(raw_input()))]
s = sorted(set([x[1] for x in a]))
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print name