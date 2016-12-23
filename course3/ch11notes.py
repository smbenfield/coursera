# Imports Regular Expressions
import re

# Searches for a matching string to a reg ex
# re.search()

# Searches for portions of a string to match a reg ex
# re.findall()

# Searches for lines with From:
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): # ^ means starts with
        print line
