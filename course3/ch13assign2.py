import urllib
import json

jsnames = list()
jscomms = list()

inputurl = raw_input("Enter URL:")

if len(inputurl) < 1 : exit()

uopen = urllib.urlopen(inputurl)
udata = uopen.read()

print 'Retrieved', len(udata), 'characters.'

try: jsload = json.loads(str(udata))
except: jsload = None

# print json.dumps(jsload, indent = 4)
for item in jsload['comments']:
    comm = item["count"]
    jscomms.append(comm)

# print jscomms

commcount = sum(jscomms)

print commcount
