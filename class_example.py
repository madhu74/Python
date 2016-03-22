'''
Created on Mar 19, 2016

@author: MADHUSUDAN
'''
class test(object):
    def __init__(self,name):
        self.c_name = name
    
    def print_1(self):
        return self.c_name
        

friends=[]
friends=list()
friends=["madhu","krsh","prvn"]
friends.append("rohit")
test_dict=dict()
test_dict={}
test_dict={"praveen":1,"krsh":2,"madhu":3}
frieds_tuples=("praveen","madhu")
#print dir(frieds_tuples)
a="madhu"
print dir(a)
madhu = test(friends)
print madhu.print_1()
print madhu.c_name
