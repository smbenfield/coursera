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

# Repeat characters (* +) return as large of a string as possible - greedy
# (?) Does not do greedy matching
# \$ = Real $ sign

# ^	           Matches the beginning of a line
# $	           Matches the end of the line
# .	           Matches any character
# \s	       Matches whitespace
# \S	       Matches any non-whitespace character
# *	           Repeats a character zero or more times
# *?           Repeats a character zero or more times (non-greedy)
# +            Repeats a character one or mormae times
# +?           Repeats a character one or more times (non-greedy)
# [aeiou]      Matches a single character in the listed set
# [^XYZ]	   Matches a single character not in the listed set
# [a-z0-9]     The set of characters can include a range
# (	           Indicates where string extraction is to start
# )	           Indicates where string extraction is to end

# Starts with (^) "X" Any character (.) Zero or more times (*) :
"^X.*:"
# Starts with (^) "X-" Any non-whitespace character (\S) One or more times (+) :
"^X-\S+:"
# One digit inside brackets, then one or more digits (+)
"[0-9]+"
# Looking for 1 or more uppercased vowel
"[AEIOU]+"
# Looking for email address formatting
"\S+@\S+"
# Begins with "From", extract email address
"^From (\S+@\S+)"
# Find an @ sign, extract until next single character is a space
"@([^ ]*)"
# Look for From and any number of characters until @, then extract until space
"^From .*@([^ ]*)"
