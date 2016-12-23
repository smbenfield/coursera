count = 0
numbr = 0
hour = []

fname = raw_input("Enter file name: ")
fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
	lsplt = line.rstrip()
	if not line.startswith("From "): continue
	lword = lsplt.split()
	lhour = lword[5].split(':')
	hour.append(lhour[0])
	count += 1
	lengl = len(hour)

slimhours = list()
for item in hour:
	if not item in slimhours:
		slimhours.append(item)
		slimhours.sort()

counts = dict()
for item in hour:
	counts[item] = counts.get(item,0) + 1

for hour in slimhours:
	print hour, counts[hour]