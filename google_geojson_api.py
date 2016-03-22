'''
Created on Mar 21, 2016

@author: MADHUSUDAN
'''
import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'
place=raw_input("Enter the location")
url = serviceurl+urllib.urlencode({'sensor':'fales','address':place})
data=urllib.urlopen(url).read()
data_js=json.loads(data)
#print data_js
#print data
#print url
print "Place id",data_js['results'][0]['place_id']