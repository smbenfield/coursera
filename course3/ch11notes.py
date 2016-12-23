# Imports Regular Expressions
import re

# Searches for a matching string to a reg ex
# Returns True/False as to whether that string contains the thing
# re.search()

# Searches for portions of a string to match a reg ex
# Returns python list of instances of said thing
# re.findall()

# Searches for lines with From:
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): # ^ means starts with
        print line


# Starts with (^) "X" Any character (.) Zero or more times (*) :
"^X.*:"
# Starts with (^) "X-" Any non-whitespace character (\S) One or more times (+) :
"^X-\S+:"
# One digit inside brackets, then one or more digits (+)
"[0-9]+"
