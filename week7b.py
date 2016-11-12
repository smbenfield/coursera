largest_so_far = None
smallest_so_far = None

def largest(n, lsf):
	if n > lsf:
		lsf = n
		return lsf
	elif n <= lsf:
		print "bug1"
		return n
	else:
		print "bug2"

def smallest(n, ssf):
	if n < ssf:
		ssf = n
		return ssf
	elif n >= ssf:
		print "bug1"
		return n
	else:
		print "bug2"

while True:
	try:
		num = raw_input("Enter a number:")
		print num
		if num == "done":
			break
		else:
			number = float(num)
			print number
			smallest_so_far = smallest(number, largest_so_far)
			largest_so_far = largest(number, smallest_so_far)
	except ValueError:
		print "I'm sorry, that's not a valid number."
		break

print "Maximum is:", largest_so_far
print "Minimum is:", smallest_so_far