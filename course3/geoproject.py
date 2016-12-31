import json
import urllib

locdct = dict()
name = None

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    usernam = raw_input("Enter Name:")
    if len(usernam) < 1 : break
    userloc = raw_input("Enter Location:")
    if len(userloc) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': userloc})

    print "Retrieving", url
    uropen = urllib.urlopen(url)
    urread = uropen.read()
    print "Retrieved", len(urread), "characters"

    try: js = json.loads(str(urread))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    locdct[usernam] = [userloc, lat, lng]
    print locdct
    locdcttxt = str(locdct)
    print locdcttxt

gptext = open('geoproject.txt', 'rw')
gpread = gptext.read()
print gpread
gptext.close()
