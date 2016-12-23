import urllib
userurl = raw_input("Input your url:")
fhand = urllib.urlopen(userurl)

for line in fhand:
    print line.strip()
