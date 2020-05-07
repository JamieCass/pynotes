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

try:
	jamie

#this except will catch any and every error
except:
	#when to try fails, it will print PROBLEM HERE
	print('PROBLEM HERE')
print('after the try')

#try and be as specific as you can when using try and except

try:
	jamie

except NameError:
	print('tried to use variable that wsnt declared')
print('after the try')

# THE BASIC SYNTAX:
# try:
# except:

# try: 
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
		#this will print none instead of the KeyError message.
d = {"name": "Ricky"}
print(get(d, "city"))
d["city"]







