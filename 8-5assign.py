count = 0
numbr = 0
test = 0
email = []
delimiter = "/n"

fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)

for line in fh:
	test += 1
	lsplt = line.rstrip()
	if not line.startswith("From "): continue
	lword = lsplt.split(" ")
	email.append(lword[1])
	count += 1
	numbr +=1
print test
print email
print "There were", count, "lines in the file with From as the first word"
