count = 0
numbr = 0
test = 0
email = []
delimiter = "/n"

fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)
fread = fh.read()
fline = fread.split(delimiter)
print fline
fleng = len(fline)
print fleng
for line in fline:
	test += 1
	if line.startswith("From "):
		lsplt = line.split()
		lword = lsplt[1]
		email.append(lword)
		print "Appended"
		count += 1
for item in email:
	print email[numbr]
	numbr +=1
print test
print email
print "There were", count, "lines in the file with From as the first word"
