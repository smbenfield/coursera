# To determine basic numerology of names
on = True
numb = 0


# Define Functions
def numletassign(n):
	n = n.lower()
	o = []
	for character in n:
		number = ord(character) - 96
		if number > 0:
			o.append(number)
	print o
	return o

def nametotal(o):
	nt = sum(o)
	print nt
	return nt

def namenumb(nt):
	nn = sum(int(digit)for digit in str(nt))
	print nn
	return nn


# Asks for Name
name = raw_input("Enter your name:")
length = len(name)

print "Your name is %s letters long." % length

output = numletassign(name)
nametotal = nametotal(output)
namenumber = namenumb(nametotal)
namenumber = namenumb(namenumber)
