# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
x = 0
numtotal = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        x = x + 1
        numline = line[20:26]
        numfloat = float(numline)
        numtotal = numtotal + numfloat
    else:
    	continue
avg = numtotal/x
print "Average spam confidence: ",avg