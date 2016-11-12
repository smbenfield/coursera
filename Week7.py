largest = None
smallest = None

def larger(n,l):
    if l is None:
        return n
    elif l > n:
        return l
    else:
        return n

def smaller(n,s):
    if s is None:
        return n
    elif s < n:
        return s
    else:
        return n

while True:
    try:
        num = raw_input("Enter a number:")
        if num == "done": 
            break
        else:
            number = float(num)
            largest = larger(number, largest)
            smallest = smaller(number, smallest)
    except ValueError:
        print "Invalid Input"
        break

print "Maximum is", int(largest)
print "Minimum is", int(smallest)
