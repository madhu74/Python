'''
Created on Mar 23, 2016

@author: MADHUSUDAN
'''
import string
alphabets_list=string.ascii_lowercase
print alphabets_list
newset=''
value_decode="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for letter in value_decode:
    if letter not in alphabets_list:
        newset=newset+letter
    elif letter=='z':
        newset=newset+'b'
        continue
    elif letter=='y':
        newset=newset+'a'
        continue
    else:
        newset=newset+alphabets_list[alphabets_list.find(letter)+2]
print newset
########
print "\nAfter doing a basic decode operation found the puzzle\n"
normal=string.ascii_lowercase
puzzle_decode='cdefghizklmnopqrstuvwxyzab'
trans_op=string.maketrans(normal,puzzle_decode)
print value_decode.translate(trans_op)
#print trans_op 