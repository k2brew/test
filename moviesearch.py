import sys
import urllib.request
import re
import json

#Ask for movie title
title = input("Please enter a movie title: ")

#Ask for which year
year = input("which year? ")

#Search for spaces in the title string
raw_string = re.compile(r' ')

#Replace spaces with a plus sign
searchstring = raw_string.sub('+', title)

#Prints the search string
print(searchstring)

#The actual query
url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

request = urllib.request.Request(url)

#response = json.load(urllib.request.urlopen(request))
response = urllib.request.urlopen(request)

#print(json.dumps(response))
print(response)
