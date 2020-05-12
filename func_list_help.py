#######################################################################
# Changine stuff in lists
#######################################################################

##########################################
# REMOVING
##########################################

eg_list = [2,4,3,3,2,5]
# Remove something from its index
.pop(1)
# would remove the second index so eg_list would look like [2,3,3,2,5]

# Remove the first instance of something
.remove(3)
# would remove the first no3 it came across, if there isnt a no3 and ERROR would pop up, so eg_list would look like [2,4,3,2,5]


##########################################
# ADDING
##########################################

instructors = []

# To add one at a time (to the end of the list)
instructors.append('Colt')
instructors.append('Blue')

# To add into the list wherever you choose. just add the index where you want it to go.
instructors.insert(1,'Fred')

# To add multiple
instructors.extend(['Colt','Blue','Lisa'])

##########################################
# NESTED LISTS
##########################################

answer = [[num for num in range(0,3)] for val in range (0,3)]

# Would look like

[[0,1,2][0,1,2][0,1,2]]


##########################################
# Only return True or things that have a value.
##########################################

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(stuff):
    return [a for a in stuff if a]

# Remember that 0, None or False have no value so wont show up as True.

##########################################
# Return if value is in both lists.
##########################################

def intersection(word1,word2):
    return[val for val in word1 if val in word2]


#######################################################################
# Functions
#######################################################################

##########################################
# *args
##########################################

#allows you to input as many arguments as you want into a function.

def feed_me(*stuff):
    for thing in stuff:
        print(f"YUMMY I EAT {thing}")
feed_me("apple", "tire", "shoe", "salmon")

# This will print 'YUMMY I EAT apple'
#                 'YUMMY I EAT tire' and so on...


##########################################
# **kwargs
##########################################

# Gathers remaining keyword arguments and puts them into a dict.

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
fav_colors(colt="royal deep amazing purple")

# This will print 'colts favorite color is purple, rubys favorite color is red' and so on

##########################################
# Parameter ordering
##########################################

# 1. parameters   2.*args   3.default parameters   4.**kwargs

def display_info(a, b, *args, instructor="Colt", **kwargs):
  # return [a, b, args, instructor, kwargs]
  print(type(args))

print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

# a - 1
# b - 2
# args (3)
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}

# print would look like this [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]

##########################################
# Tuple/list unpacking
##########################################

def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

# sum_all_values(1,30,2,5,6)

nums = [1,2,3,4,5,6]
sum_all_values(*nums)

# use the '*' to unpack everything in a list/tuple like in nums.
# it makes it into individual items.


##########################################
# Dictonary unpacking
##########################################

# same as list unoacking but use (**)
# e.g
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

display_names(names) # nope..
display_names(**names)  # yup!


#######################################################################
# Lambdas and Built in Functions
#######################################################################

##########################################
#Lambdas (not used as much really)
##########################################

# like a function but not name and has to be on one line.
# useful for one time functions.
###########################

#e.g

# A regular named function
def square(num): return num * num

# An equivalent lambda, saved to a variable
square2 = lambda num: num * num

# Another lambda
add = lambda a,b: a + b

###########################

#e.g 2

import tkinter as tk
# DON'T WORRY ABOUT ANY OF THIS CODE
root = tk.Tk()#=====================
frame = tk.Frame(root)#=============
frame.pack()#=======================
# DON'T WORRY ABOUT ANY OF THIS CODE

# Don't need this function if we use a lambda
# def say_hi():
#     print("HELLO!")

button = tk.Button(frame,
                   text="CLICK ME",
                   fg="red",
                   command=lambda: print("Hello"))
                   # it was command=say_hi but say_hi isnt needed if we use lambda.



# DON'T WORRY ABOUT ANY OF THIS CODE
button.pack(side=tk.LEFT) #=========
root.mainloop() #===================
# DON'T WORRY ABOUT ANY OF THIS CODE



##########################################
# Map
##########################################

#e.g
nums = [2,4,6,8]

# map alows you to go through a list 1 by one and do whatever your funcction or lambda wants.
# so we want to double every number in nums... this is how we do it.
doubles = list(map(lambda x: x*2, nums))

# need to make the result a list.. otherwise you need to redo the lambda every time.

##########################################
# e.g 2

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Cole', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'}
]

# we want just the first names so we would do it like this..

first_names = list(map(lambda x: x['first'], names))

##########################################
# e.g 3

# takes a list of numbers and takes away 1 from each one.
def decrement_list(nums):
    return list(map(lambda n: n-1,nums))




##########################################
# Filter
##########################################

# similar to map really.

# e.g

l = [1,2,3,4]

# the filter is going to return any even numbers. (still have to use the list function to return a list)
evens = list(filter(lambda x: x % 2 == 0, l))

##########################################
# e.g 2
names = ['austin','penny','anthony','angel','billy']

# i want all names beginning with a using filter.

a_names = list(filter(lambda n: n[0]=='a', names))

##########################################
# e.g 3

# map and filter together
# i want to return a list with names that have less than 5 characters.

names = ['Lassie', 'Colt', 'Rusty']

list(map(lambda name: f"Your instructor is {name}",
    filter(lambda value: len(value) < 5, names)))

# the filter runs first, then only returns what name has less than 5 characters.

##########################################
# e.g 4 with list comp examples as well.

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
    filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]


##########################################
# Any and all
##########################################

##########
# ALL every item in a list must be true.

#e.g

all([num for num in [2,4,6,10,14] if num % 2 == 0])

# or

nums = [2,4,6,18,30]
all([num % 2 == 0 for num in nums ])

# this would only print True if ALL numbers where even!!

##############################
# ANY item in a list can be True.

any([0,1,2,3]) # True

any([val for val in [1,2,3] if val > 2]) # True

any([val for val in [1,2,3] if val > 5]) # False

any([num % 2 == 1 for num in nums]) # True


##########################################
# Sorted
##########################################

# can use this to sort all numbers into order. can us a tuple or a list.
# the .sort() wont take in a tuple, only a list.


# e.g

# sorted (works on anything that is iterable)
nums = [2,5,1,6,]

sorted(nums) # [1,2,5,6]

# but it wont save it so if you print(nums) again it wont be in order.

sorted(nums, reverse = True) #[6,5,2,1]


#######################################

#e.g 2

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
sorted(users,key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)

# ANOTHER EXAMPLE DATA SET==================================
songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])


##########################################
# Min Max
###########################################
names = ['Jamie', 'Mum', 'Ollivander', 'Sophie']

# if we want the min or max anf have the name printed with need to do this.

max(names, key=lambda n: len(n))
min(names, key=lambda n: len(n))

# we need to have a key! cant just len becasue it will give us the number of characters.

####################
# e.g 2

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min(len(name) for name in names) # 3

# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA


###########################################
# Reversed
###########################################

# simialr to slicing if you dont interate over something.
'hello'[::-1]# 'olleh'

#e.g

reversed('hello')
list(reversed('hello'))# ['o','l','l','e','h']
''.join(list(reversed('hello')))# 'olleh'


for x in reversed range(0,10):
    print(x)
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0


###########################################
# len .... EXTENDED
###########################################

class SpecialList:

    def __init__(self, data):
        self.__data = data

    def __len__(self):  # JUST LOOK AT THIS LINE
        return 50 # ive just told it that the len is 50 no matter how mnay items in the list!!


l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5])

print(len(l1)) #50
print(len(l2)) #50



###########################################
# abs()   sum()   round()
###########################################

# abs (stand for absolute value)
#so if its negative the abs would still be the same number.

abs(-8) # 8
abs(8) # 8


#sum (takes an interable and an optional start)
#returns sum of start and items of an iterable from left to right and returns the total

sum([1,2,3]) # 6
sum([1,2,3], 10) # 16... this will add everyhting to 10 (because we defined the start point)


#round (return a rounded number to specified number of digits after decimal point)

round(10.2) # 10
round(10.234343, 2) #10.23 will round it to 2 decimal places.


# function to take dict or names and join first and second

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_fullNames(nam):
    return list(map(lambda x: '{} {}' .format(x['first'], x['last']), nam))


extract_fullNames(names)





###########################################
# ZIPPING
###########################################

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)




