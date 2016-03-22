'''
Created on Mar 20, 2016

@author: MADHUSUDAN
'''
import urllib
import xml.etree.ElementTree as et
url_handle = urllib.urlopen("http://python-data.dr-chuck.net/comments_248182.xml").read()
xml_tree = et.fromstring(url_handle)
#print url_handle
sum=0
items_required=xml_tree.findall("comments/comment")
for item in items_required:
    sum = sum+int(item.find("count").text)
print sum