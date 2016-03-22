'''
Created on Mar 20, 2016

@author: MADHUSUDAN
'''
#bs4 is the beautiful soup library
import urllib
from bs4 import BeautifulSoup
#from bs4 import BeautifulSoup
#from bs4 import BeautifulStoneSoup
import scipy
url=raw_input("Enter the URL")
print scipy.absolute(-1.0009)
count= int(raw_input("Enter count"))
position = int(raw_input("Enter Position"))
print "Retrieving:",url
for i in range(0,count):
    web_handle=urllib.urlopen(url)
    data = web_handle.read()
    soup_test=BeautifulSoup(data,"html.parser")
    tags = soup_test('a')
    print "Retrieving:",tags[position-1].get('href', None)
    url=tags[position-1].get('href', None)