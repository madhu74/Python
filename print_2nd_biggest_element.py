n=int(raw_input())
lst=raw_input()
numb=map(int,lst.split())
sbig=-600000
big=-600000
for i in numb:
    if i>big:
        big,sbig = i,big
    elif i < big and i > sbig:
        sbig=i
print sbig