count = 0
numbr = 0
email = []

fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)

for line in fh:
	lsplt = line.rstrip()
	if not line.startswith("From "): continue
	lword = lsplt.split(" ")
	email.append(lword[1])
	print lword[1]
	count += 1
	lengl = len(email)
print "There were", count, "lines in the file with From as the first word"
