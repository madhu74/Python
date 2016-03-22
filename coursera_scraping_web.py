'''
Created on Mar 20, 2016

@author: MADHUSUDAN
'''
#bs4 is the beautiful soup library
import urllib
from bs4 import BeautifulSoup
#from bs4 import BeautifulSoup
#from bs4 import BeautifulStoneSoup
web_handle=urllib.urlopen("http://python-data.dr-chuck.net/comments_248185.html")
data = web_handle.read()
soup_test=BeautifulSoup(data,"html.parser")
tags = soup_test('span')
total=0
count=0
for tag in tags:
    count+=1
    total+= float((tag.contents[0]))
print "Count",count
print "Sum",total