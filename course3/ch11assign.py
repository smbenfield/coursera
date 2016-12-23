import re

numinteg = list()

filename = raw_input('Input filename:')
handle = open(filename)
fileread = handle.read()

numstrin = re.findall('[0-9]+',fileread)
for item in numstrin:
    numinteg.append(int(item))

print numinteg
print sum(numinteg)
