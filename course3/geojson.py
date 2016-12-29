import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    # User input
    address = raw_input('Enter location: ')
    # Breaks if no input
    if len(address) < 1 : break

    # Encodes url to fit rules
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    # Creates opening to URL
    uh = urllib.urlopen(url)
    # Reads URL
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    # Loads URL into readable data
    try: js = json.loads(str(data))
    # try/except prevents errors
    except: js = None
    # Provides error
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    # Prints in readable form
    print json.dumps(js, indent=4)

    # Searches for relevant info
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
