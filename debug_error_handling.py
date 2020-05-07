#######################################################################
# Most common errors
#######################################################################

##########################################
# SyntaxError
##########################################

#Occurs when theres a problem with the syntax (not valid python)

None = 1 
#SyntaxError: invalid syntax


##########################################
# NameError
##########################################

#Occurs when a variable is not defined 

test 
#NameError: name 'test' is not defined


##########################################
# TypeError
##########################################

#Occurs when operation or function is applied to wrong type

len(5) 
#TypeError: object of type 'int' has no len()


'awesome' + [] 
#TypeError: cannot concatenate 'str' and 'list' objects



##########################################
# IndexError
##########################################

#Occurs when you try and access an element outside of a list index

name = 'jamie'
name[6]
#IndexError: string index out of range


##########################################
# ValueError
##########################################

#Occurs when a built in opperation or function recieves and argument that has right type but inapropriate value

int('foo')
#ValueError: invalid literal for int() with base 10: 'foo'


##########################################
# KeyError
##########################################

#Occurs when a dictionary doesnt have a specifin key

d = {}
d['foo']
#KeyError: 'foo'


##########################################
# AttributeError
##########################################

#Occurs when a variable doesnt have an attribute

'awesome'.foo
#AttributeError: 'str' object has no attribute 'foo'



#######################################################################
# Raising our own errors
#######################################################################

#Useful for when people use our code, we can create our own kinds of exception and error messages

#Make them helpful to whoever will be reading and using your code

raise ValueError('invalid value')

def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		# now we can raise an error that relates to text not being a str
		raise TypeError("text must be instance of str")
	if color not in colors:
		# we can raise an error if the color isnt in colors.
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

colorize([], 'cyan')
# colorize(34, "red")



#######################################################################
# Handling errors (try, except, else and finally)
#######################################################################

#Try and except allow the code to run past the first error and let you know where it is

#not the best example but it still helps a little

# THE BASIC SYNTAX:
# try: (the code and see if there are errors)
# except: (comes up with error if theres any found or any specific if you specified)
# else: (will work whenever theres not an error)
# finally: (runs no matter what)


#######################

try:
	jamie

#this except will catch any and every error
except:
	#when to try fails, it will print PROBLEM HERE
	print('PROBLEM HERE')
print('after the try')


#try and be as specific as you can when using try and except

#######################

try:
	jamie

except NameError:
	print('tried to use variable that wsnt declared')
print('after the try')

#######################

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
		#this will print none instead of the KeyError message.
d = {"name": "Ricky"}
print(get(d, "city"))
d["city"]

#######################

while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break
	finally:
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")

# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")

#######################

# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be ints or floats")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")


print(divide(1,2))
print(divide(1,'a'))
print(divide(1,0))



#######################################################################
# Debugging with pdb
#######################################################################

#pdb (python debugger)

#set breakpoints in code we use pdb
#pauses your code and you can look into it all before going onto the next line/step

# FIRST EXAMPLE:
# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)


# Be careful with variable names! 
#(c below for instance just continues the code from the break)

def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace() 

    return a + b + c + d
add_numbers(1,2,3,4)

# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

