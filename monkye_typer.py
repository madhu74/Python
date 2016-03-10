'''
Created on Feb 22, 2016

@author: MADHUSUDAN
'''
import random
# monkey_typer
def monkey_typer(n):
    mnky_word=""
    alphabets="abcdefghizhlmnopqrstuvwxyz "
    #alphabets.split()
    for _ in range(n):
        mnky_word=mnky_word+alphabets[random.randrange(n-1)]
    return mnky_word

def score(monkey_word):
    expword="methinks it is like a weasel"
    count=0
    for i in range(len(expword)):
        if(expword[i]==monkey_word[i]):
            count+=1
    return count/len(expword)
#if len("methinks it is like a weasel")==len(monkey_typer(28)):
#    print "A ok"
new_string=monkey_typer(28)
#print score(monkey_typer(28))
new_score=score(new_string)
best=0
iteration=0
while new_score < 1 and iteration<1000000:
    if new_score>best:
        best = new_score
        print best,new_string
    new_string= monkey_typer(28)
    new_score = score(new_string)
    iteration+=1
print "done"

