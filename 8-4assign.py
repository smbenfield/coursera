larr = []
fname = raw_input("Enter file name: ")
fh = open(fname)
flst = fh.read()
lst = flst.split()
for line in lst:
	lstr = line.strip()
	if lstr in larr:
		continue
	else:
		larr.append(lstr)
	larr.sort()
print larr