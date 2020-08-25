#######################################################################
# Regular Expressions (REGEX)
#######################################################################
##########################################
 # What are Regular Expression
##########################################
# - A way of desscribing patterns within search strings
https://docs.python.org/3/library/re.html #(link to regex documentation)

##########################################
 # EMAILS
##########################################
# - Starts with 1 or more letter, number, +, _, -,.
# - A single @ sign then
# - 1 or more letter, number, or - then
#- A single dot then
# - Ends with 1 or more letter, number, -, or .

# Regular expression would look like this..
#(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

##########################################
 # Potential use cases
##########################################
# - Credit card number validating
# - Phone number validating
# - Advanced find/replace in text
# - Formatting text/output
# - Syntax highlighting

##########################################
 # Some regex syntax (LOOK AT A CHEAT SHEET FOR MORE)
##########################################
http://www.rexegg.com/regex-quickstart.html (cheatsheet)
https://pythex.org/ (online tester)
#----- some characters -----
# '\d' digit 0-9
# '\w' letter, digit or underscore
# '\s' whitespace character
# '\D' not a digit
# '\W' not a word character
# '\S' not a whitespace character
# '.' any character except line break

#----- quantifers -----
# '+' one or more
# '{3}' exactly x times. {3} - 3 times
# '{3,5}' three to five times
# '{4,}' four or more times
# '*' zero or more times
# '?' once or none (optional)

#----- anchors and boundaries -----
# '^' start of string or line (the '^' also means not.. [^@$] would match anything thats neither @ nor $ sign)
# '$' end of string or line
# '\b' word boundary
# Using the ^ and $.. This is only good to check if the string or line is ONLY whatever is in the between them.
# '|' LOGICAL OR
##########################################
 # REGEX with Python
##########################################
# import regex module
import re

# define our phone number regex
phone_no = re.compile(r'\d{3} \d{3}-\d{4}')
email = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# search a string with out regex
res = phone_no.search('Call me at 415 555-4242!')
res
email.search('Email me at jamies_email@gmail.com')

#LOGICAL OR e.g
test_search = re.compile('(\(\d{3}\)|\d{3}) \d{3}-?\d{4}') #this will search for a number that has () or not.
test_search.search('425 354-0998 (415) 354-0998')
