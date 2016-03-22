'''
Created on Mar 21, 2016

@author: MADHUSUDAN
'''
import urllib
import json

url_handle=urllib.urlopen("http://python-data.dr-chuck.net/comments_248186.json").read()
js=json.loads(url_handle)
total=0
count=0
for item in js['comments']:
    count+= 1
    total+= int(item['count'])
print count
print total