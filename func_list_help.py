##################################################
# Changine stuff in lists
##################################################

#####################
# REMOVING
#####################

eg_list = [2,4,3,3,2,5]
# Remove something from its index
.pop(1)
# would remove the second index so eg_list would look like [2,3,3,2,5]

# Remove the first instance of something
.remove(3)
# would remove the first no3 it came across, if there isnt a no3 and ERROR would pop up, so eg_list would look like [2,4,3,2,5]


#####################
# ADDING
#####################

instructors = []

# To add one at a time (to the end of the list)
instructors.append('Colt')
instructors.append('Blue')

# To add into the list wherever you choose. just add the index where you want it to go.
instructors.insert(1,'Fred')

# To add multiple
instructors.extend(['Colt','Blue','Lisa'])

#####################
# NESTED LISTS
#####################

answer = [[num for num in range(0,3)] for val in range (0,3)]

# Would look like

[[0,1,2][0,1,2][0,1,2]]


#####################
# Only return True or things that have a value.
#####################

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(stuff):
    return [a for a in stuff if a]

# Remember that 0, None or False have no value so wont show up as True.

#####################
# Return if value is in both lists.
#####################

def intersection(word1,word2):
    return[val for val in word1 if val in word2]


##################################################
# Functions
##################################################

#####################
# *args
#####################

#allows you to input as many arguments as you want into a function.

def feed_me(*stuff):
    for thing in stuff:
        print(f"YUMMY I EAT {thing}")
feed_me("apple", "tire", "shoe", "salmon")

# This will print 'YUMMY I EAT apple'
#                 'YUMMY I EAT tire' and so on...


#####################
# **kwargs
#####################

# Gathers remaining keyword arguments and puts them into a dict.

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
fav_colors(colt="royal deep amazing purple")

# This will print 'colts favorite color is purple, rubys favorite color is red' and so on

#####################
# Parameter ordering
#####################

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

#####################
# Tuple/list unpacking
#####################

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


#####################
# Dictonary unpacking
#####################

# same as list unoacking but use (**)
# e.g
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

display_names(names) # nope..
display_names(**names)  # yup!


##################################################
# Lambdas and built in Functions
##################################################

#####################
#Lambdas (not used as much really)
#####################

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
