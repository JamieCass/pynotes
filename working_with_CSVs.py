#######################################################################
# Working with CSV files
#######################################################################

##########################################   READING CSV FILES   ##########################################

# Python has a built-in CSV module to read/write CSVs mmore easily
# There are 2 modules you can use to read a csv file..
# Readers can accept a delimiter kwarg in case data isnt seperated by commas (you just need to specify when you read the file)

# 1--- 'reader' lets you iterate over rows of a CSV file as lists

# 2--- 'DictReader' lets you iterate over rows of a CSV as OrderedDicts

# ---- reader e.g ----
from csv import reader
with open('file_name.csv') as file:
# open('file_name.csv', delimeter = '|') # e.g of setting the delimeter..
    csv_reader = reader(file)
    for row in csv_reader:
        # each row is a list!
        print(row)

# ---- DictReader e.g ----
from csv import DictReader
with open('file_name.csv') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row)

#----------   EXAMPLES (of 'reader' and 'DictReader')!   ---------

# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
with open("fighters.csv") as file:
    data = file.read()

# Using reader
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) #To skip the headers (so the first list will be skipped i.e 'name', 'country', 'height (in cm)')
    for fighter in csv_reader:
    	# Each row is a list
    	# Use index to access data
    	print(f"{fighter[0]} is from {fighter[1]}") # we can print out what where each fighter is from!

# Example where data is cast into a list
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name'], ' : ', row['Country']) #Use keys to access data

##########################################   WRITING CSV FILES   ##########################################
#                                             (using lists)
# 'writer' - creates a writer object for writing to CSV
# 'writerow' - method on a writer to write a row to the CSV

#----------   EXAMPLE (of 'writer')!   ---------

from csv import writer, DictWriter
#Version using writer
with open("cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])

#----------   EXAMPLES (uppercase everything in a CSV file and save it as another)   ----------

from csv import reader, writer
# using nested with statements
with open('fighters.csv') as file:
	csv_reader = reader(file) #data never converted to list
	with open('screaming_fighters.csv', "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])


# Other approach, with only 1 file open at a time
with open('fighters.csv') as file:
	csv_reader = reader(file)
	# data converted to list and saved to variable
	fighters = [[s.upper() for s in row] for row in csv_reader] # we save fighters as a variable so we can access it in the code below

with open('screaming_fighters.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)

##########################################   WRITING CSV FILES   ##########################################
#                                           (using Dictionaries)

# 'DictWriter' - creates a writer object for writing using dictionaries
# 'fieldnames' - kwarg for the DictWriter specifying headers
# 'writeheader' - method on a writer ti write header row
# 'writerow' - method on a writer to write a row based on a dictionary

#----------   EXAMPLE (of 'DictWriter')!   ---------
# Version using DictWriter
with open("cats.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader() # write all the headers to the file
	csv_writer.writerow({ # now we can put it whatever name, age and breed we want
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})

from csv import DictReader, DictWriter

def cm_to_in(cm):
	return float(cm) * 0.393701 # need to make sure whatever is being passed into the function is a float (it wouldnt multiply a str)

with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
	headers = ("Name","Country","Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_to_in(f["Height (in cm)"])
		})

##########################################   NEW TASK   ##########################################

# Implement a funciton that takes a first name and last name and add a new user to the 'users.csv' file.

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
import csv
def add_user(first, last):
    with open("users.csv", "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first, last])

add_user('Jamie', 'Cass')
##########################################   NEW TASK   ##########################################

# Implement a funciton that prints out all of the first and last names in 'users.csv' file.

'''
print_users() # None
# prints to the console:
# Colt Steele
'''
import csv
def print_users():
    with open('users.csv') as f:
        re = csv.DictReader(f)
        for row in re:
            print ('{} {}'.format(row['First Name'], row['Last Name']))

print_users()
##########################################   NEW TASK   ##########################################

# Implement a funciton that takes in a first name and a last name and searches for a user with that name.
# If the user is found it returns the index where the user is found. Otherwise it returns a message stating the user wasnt found.

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

import csv
def find_user(first, last):
    first_name = first
    last_name = last
    with open('users.csv') as f:
        reader = csv.reader(f)
        for (index, row) in enumerate(reader):
            first_name = first == row[0]
            last_name = last == row[1]
            if first_name and last_name:
                return index
        return '{} {} not found.'.format(first, last)

find_user('Jamie', 'Cass')

##########################################   PICKLING   ##########################################

# When you pickle something, it saves it as binary, so you cant actually read it until you unpickle it!!
# This is only good for python really.

import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
with open("pets.pickle", "wb") as file: # needs to have the .pickle at the end of the file name and then the 'wb' for write binary
	pickle.dump(blue, file) # we then need to 'dump' it into the file, we need to say what we are dumping, then specify that we want to put it into the pickle file we opened in the line above.

# To unpickle something:
with open("pets.pickle", "rb") as file: # open the file up with the .pickle at the end of it, and also 'rb' for read binary.
	zombie_blue = pickle.load(file)
	print(zombie_blue) # Blue is a Cat
	print(zombie_blue.play()) # Blue plays with String

##########################################   JSON PICKLING   ##########################################

# e.g of json

import json

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

# json.dumps returns a JSON STRING:

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# results in '["foo", {"bar": ["baz", null, 1.0, 2]}]'

j = json.dumps(c.__dict__)
# results in '{"name": "Charles", "breed": "Tabby"}'

################################################################################

# this is more readable when if you want to read the file and you can use it for other languages not just python.
# e.g of json pickle

import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

# To JSONPICKLE 'c' the cat:
with open("cat.json", "w") as file:
	frozen = jsonpickle.encode(c) # you need to encode the file insteasd of writing it as binary
	file.write(frozen)

# To bring back 'c' the cat using JSONPICKLE
# with open("cat.json", "r") as file:
# 	contents = file.read()
# 	unfrozen = jsonpickle.decode(contents) # Decode the file
# 	print(unfrozen)

##########################################   NEW TASK   ##########################################

# Implement a funciton that takes in an old first name, an old last name, a new first name and a new last name.
# Updates the users.csv file so that any user whose first and last name match the old ones are updates to the new first and last names.
# The function should return a count of how manys users were updated.

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

def update_users(first, last, new_first, new_last):
    with open('users.csv') as file:
        reader = csv.reader(file)
        rows = list(reader)

    count = 0
    with open('users.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == first and row[1] == last:
                writer.writerow([new_first, new_last]) # write the new first and last names
                count += 1
            else:
                writer.writerow(row) # if there arent any new names to write,  re-write the old ones...
        return f'Users updated: {count}'

update_users('Luke', 'Skywalker','Jamie', 'Cass')
update_users('Alan', 'Long', 'Obi', 'Wan')

##########################################   NEW TASK   ##########################################
# Implement a function that will take a first name and a last name then update the users.csv file so that any user whose name matches are removed.
# The function should also return the number of users removed.

count = 0
def del_users(first, last):
    global count
    with open('users.csv') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('users.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == first and row[1] == last:
                count += 1
            else:
                writer.writerow(row)
        return f'Users updated: {count}.'

del_users('Jamie', 'Cass')
del_users('Grace', 'Hopper')
del_users("Not", "Here")


add_user('Jamie', 'Cass')
add_user('Grace', 'Hopper')
