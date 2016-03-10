'''
Created on Feb 22, 2016

@author: MADHUSUDAN
'''
def gcd(m,n):
        while m%n!=0:
            old_m=m
            old_n=n
            m=old_n
            n=old_m%old_n
        return n
    
class Fraction(object):
    '''
    classdocs This is a simple class program that defines about abstract datatypes here we are implementing
    a fraction function which is mainly used to show fraction in their exact form 
    '''
    def __init__(self, top,bottom):
        '''
        Constructor defines the way in which the data-objects are created
        '''
        self.num=top
        self.den=bottom
     
    def show(self):
        print self.num,"/",self.den
        
    def __str__(self): #overriding a standard string method of the class to print the value of the class
        return str(self.num)+"/"+str(self.den) 
    
    def __add__(self,other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common=gcd(new_num,new_den)
        return Fraction(new_num/common,new_den/common)
    
    def __sub__(self,other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common=gcd(new_num,new_den)
        return Fraction(new_num/common,new_den/common)
    
    def __mul__(self,other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common=gcd(new_num,new_den)
        return Fraction(new_num/common,new_den/common)
    
    def __div__(self,other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common=gcd(new_num,new_den)
        return Fraction(new_num/common,new_den/common)
    
    def __eq__(self,other_function):
        new_val1 = self.num * other_function.den
        new_val2 = self.den * other_function.num
        
        return new_val1==new_val2
    
    def __gt__(self,other_function):
        new_val1 = self.num * other_function.den
        new_val2 = self.den * other_function.num
        
        return new_val1 > new_val2
    
    def __lt__(self,other_function):
        new_val1 = self.num * other_function.den
        new_val2 = self.den * other_function.num
        
        return new_val1 < new_val2

''''Creating the instance of the Fraction class i.e objects and constructor is invoked''' 

my_fraction_1 = Fraction(1,2)
my_fraction_2 = Fraction(1,4)
#print my_fraction_1 # This can only show the actual reference that it is stored in the variable i.e the address of the object my_fraction
#my_fraction_1.show()
print my_fraction_1 + my_fraction_2
if my_fraction_1==my_fraction_2:
    print "Works :D"
print my_fraction_1 < my_fraction_2   
print my_fraction_1 > my_fraction_2
print my_fraction_1 * my_fraction_2
print my_fraction_1 / my_fraction_2

#print 12 % 14
