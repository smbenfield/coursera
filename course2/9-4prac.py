count = 0
numbr = 0
email = []

fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
	lsplt = line.rstrip()
	if not line.startswith("From "): continue
	lword = lsplt.split(" ")
	email.append(lword[1])
	count += 1
	lengl = len(email)


counts = dict()
for item in email:
	counts[item] = counts.get(item,0) + 1

bigcount = None
bigemail = None

for item,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = item
		bigcount = count

print bigword,bigcount
