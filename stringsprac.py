# defines initial variables
letter = int(0)
letterstring = None
vowels = int(0)
consonants = int(0)
spaces = int(0)
on = True
numb = int(0)

# defines function
def letct(i,l):
	l = l - 1
	print l
	return l

def letstr(i,l,let):
	let = i[l].upper()
	print let
	return let

def vowelcount(i,let,l,v):
	if let in ["A", "E", "I", "O", "U"]:
		v += 1
		print "Vowel number:", v
		return v
	else:
		return v

def spacecount(i,let,l,s):
	if let in " ":
		s += 1
		print "Space number:", s
		return s
	else:
		return s
	
def consonantcount(i,let,l,c):	
	if let in ["A", "E", "I", "O", "U", " "]:
		return c
		print c
	else:	
		c += 1
		return c
		print c
# The quick brown fox jumped over the lazy dog
inwords = raw_input("Enter text:")

print len(inwords)
numb = len(inwords)
letter = int(numb)

while on is True:
	# stops the loop
	if numb <= 0:
		break
	numb = numb - 1

	# function execution
	# letter changing
	letter = letct(inwords, letter)
	letterstring = letstr (inwords, letter, letterstring)
	vowels = vowelcount(inwords, letterstring, letter, vowels)
	consonants = consonantcount(inwords, letterstring, letter, consonants)
	spaces = spacecount(inwords, letterstring, letter, spaces)

print "Number of Consonants:", consonants
print "Number of Vowels:", vowels
print "Number of Spaces:", spaces
