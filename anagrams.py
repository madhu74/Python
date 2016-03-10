'''
Created on Mar 2, 2016

@author: MADHUSUDAN
'''
'''This is a program to check is two strings are anagram of each other example 'heart' and 'earth' are 
examples of anagram'''
#the method to be used are check off method
def anagram_solution1(s1,s2):
    a_list =list(s2)
    pos1=0
    stillOk=True
    while pos1 < len(a_list) and stillOk:
        found = False
        pos2=0
        while pos2 < len(s1) and not found:
            if a_list[pos1] == s1[pos2]:
                found= True
            else:
                pos2 +=1
        if found:
            a_list[pos1]=None
            pos1 = pos1+1
        else:
            stillOk=False
    return stillOk
print anagram_solution1('mahu','hmua')