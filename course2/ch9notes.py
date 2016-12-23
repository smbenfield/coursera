#purse = dict()

#purse['money'] = 40
#purse['candy'] = 2
#purse['condoms'] = 1

#print purse

#purse['candy'] = purse['candy'] + 2

#print purse

counts = dict()
print 'Enter a line of text:'
line = raw_input().upper()
words = line.split()
print 'Words:', words

print 'Counting...'
for word in words:
	counts[word] = counts.get(word,0) + 1

print 'Counts', counts

for key in counts:
	print key, counts[key]

name = raw_input('Enter file:')
handle = open(name,'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword,bigcount