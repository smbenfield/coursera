# File input
name = raw_input('Enter file:')
name = "mbox-short.txt"
handle = open(name,'r')
text = handle.read()
email = list()
# words = text.split()

for line in text:
	if line.startswith("From "): 		
		lemail = lword[1]
		print lemail
		email.append(lemail)
print email

counts = dict()
for word in email:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword,bigcount