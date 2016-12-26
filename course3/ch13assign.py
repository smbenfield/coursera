import xml.etree.ElementTree as ET
import urllib

numlst = list()
# Asks for URL
url = raw_input("Enter URL:")

# Reads URL
input = urllib.urlopen(url).read()

# Creates object
stuff = ET.fromstring(input)
# Creates list of all instances of user within users
lst = stuff.findall('comments/comment')
# Prints length of list
print 'Count:', len(lst)

#Loops through list and prints attributes and such of users
for item in lst:
    comnum = item.find('count').text
    comnum = int(comnum)
    numlst.append(comnum)
numsum = sum(numlst)
print numsum
