# JSON has two basica things and stuff
# Lists/Arrays and Dictionaries/Objects/Hashmaps
# Syntax is very python-y

import json
data = '''{
    "name" : "Chuck",
    "Phone": {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
# Creates dictionary and looks into dictionary below
print 'Name:', info["name"]
print 'Hide:', info ["email"] ["hide"]
# So in JSON, there are dictionaries set into dictionaries?

# API = Application Program Interface
# Defined set of rules to interface with an app prog
# SOAP = OLD AND OVERLY COMPLEX
# REST = Representational State Transfer (resource focused)
# Makes interaction as the web functions

# Geocoding API
# googleapis.com
