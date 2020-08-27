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
# '\b' word boundary (space, start or end of a line)
# Using the ^ and $.. This is only good to check if the string or line is ONLY whatever is in the between them.
# '|' LOGICAL OR
##########################################
 # REGEX with Python
##########################################
# import regex module
import re
# the r stands for raw string, if it wasnt at the beginning, you would have to do 2 '\' for python to recognise it as a backslash
# define our phone number regex
phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
email = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# search a string with out regex
res = phone_regex.search('Call me at 415 555-4242!')
res.group()
email.search('Email me at jamies_email@gmail.com')

##########################################
 # Validating phone numbers with python
##########################################
# get 1 phone number at a time from a  string
def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

extract_phone('my numbers is 878 009-3847')
print(extract_phone('my numbers is 746 837-938373827'))

# get multiple phone numbers in a string
def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)
extract_all_phones('my number is: 934 938-9927 or 836 837-3827')

# return True if the sstring is only a phone number and nothing else
def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False

def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input) # we can use full match instead of search woth the '^' and '$' at the start and end of the string.
    if match:
        return True
    return False

##########################################
 # Parsing URLs with python
##########################################

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)') # we put the '*' at the end because its optional 1 or more.
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
# we have put perens arpung each group so we can get the info for each group
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())

##########################################
 # Symbolic group names
##########################################

def parse_name(input):
	name_regex = re.compile(r'^(Mr\.*|Mrs\.*|Ms\.*|Mdme\.*) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first')) # labeled by using the '?P<first>' in our name_regex
	print(matches.group('last'))

parse_name("Mrs. Tilda Swinton")

parse_name('Mr Jamie Losks')

##########################################
 # Regex compilation flags
##########################################
# Verbose flag can be 're.VERBOSE' or re.X
# Ignorecase flag can be 're.IGNORECASE' or 're.I'

# Without Verbose Flag...
# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
import re
pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.X | re.I) # if you want to use both flag you need to use the '|' and that will use both flags!!

match = pattern.search("ThomaS123@Yahoo.com")
print(match.group())
print(match.groups())

##########################################
 # Regex substitution basics (.sub)
##########################################
# We can use sub to change regex matches in a string
# you need to use the ('pattern of the REGEX'.sub('what we replace matches with', from the input))
# \g<number of group> keeps the group we want and then we can change anyting else that matches the regex
text = 'Last night Mrs. Daisy and Mr. White mudered Mr. Chow'

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I) #this will search for all names with IGNORECASE
result = pattern.sub('*****', text) # we change the names to '*****'
result_2 = pattern.sub('\g<1> ***** ', text) # we use the '\g<1>' to keep the first group the same then we put whatever we are changing after..
result_3 = pattern.sub('\g<1> \g<2>', text) # we put the first letter of the name into a seperate group, so now, we can just have the title and first letter shown instead of the whole name.

result # '*****' replaces the title and name
result_2 # '*****' replaces the name but not the title
result_3 # shows just the title and first letter of the name.

##########################################   NEW TASK   ##########################################
# function that accepts a single string and return True if the string is formatted as time

def is_valid_time(time):
    time_test = re.compile(r'^\d{1,2}:\d{2}$')
    if time_test.search(time):
        return True
    return False

is_valid_time('1:52')
is_valid_time('134:56')

##########################################   NEW TASK   ##########################################
# function that accepts a string and returns a list if the binary bytes conained in the string.
# each string is just a combination of eight 1's or 0's

def parse_bytes(input):
    bytes_regex = re.compile(r'\b[01]{8}\b') # remember a word boundary is a space or the start/end of a line.
    match = bytes_regex.findall(input)
    return match

parse_bytes('my data is: 10010110 10010101')
parse_bytes('10010010 873 10010')

##########################################   NEW TASK   ##########################################
# function that checks to see if a string matches a date format of 'dd/mm/yyyy'
# it should also work with 'dd.mm.yyy' or 'dd,mm,yyyy' and should return a dictionary of the d, m and y

def parse_date(input):
    date_regex = re.compile(r'^(?P<day>\d{2})[/.,](?P<month>\d{2})[/.,](?P<year>\d{4})$')
    match = date_regex.search(input)
    if match:
        return {
                'd': match.group('day'),
                'm': match.group('month'),
                'y': match.group('year')
        }
    return None
parse_date('20,08,1919')
parse_date('20.08.199919')

##########################################   NEW TASK   ##########################################
# function that will replace any profanity with the word 'CENSORED'
# this includes 'fracking', 'fracker', 'frack' etc..

def censor(input):
    censor_regex = re.compile(r'(frack[a-z]*)', re.I)
    result = censor_regex.sub('CENSORED', input)
    return result

censor('youre a fracking idiot')
