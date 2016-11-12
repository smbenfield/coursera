#!/usr/bin/python

name = raw_input('Enter file:')
handle = open(hame, 'r')
text = handle.read()
words = text.split()
counts = dict()
for words in words:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword,bigcount