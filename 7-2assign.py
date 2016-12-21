# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        numline = line[20:26]
        print numline
        floatline = numline.float()
        print floatline
print "Done"
