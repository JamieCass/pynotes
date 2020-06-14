#######################################################################
# Decorators
#######################################################################
##########################################
#Higher order functions (prep for decorators.
##########################################
#wont really use this but its useful to know., and it helps with decorators...
#we can nest functions inside one another.. this is a good example
from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg
    #this will only return a print statment pretty much.
    result = get_mood() + person
    return result

greet('Jamie')

#we can have a function return a function.
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHA', 'lol', 'tehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())

##########################################
#inner functions can access outer function scope
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHA', 'lol', 'tehehe'))
        #person is in the outer function not in the inner function.
        return f'{laugh} {person}'

    return get_laugh

laugh_at = make_laugh_at_func('Sophie')
laugh_at()

##########################################
#What are Decorators????
##########################################
#decorators are Functions
#the wrap other functions and enhance their behaviour
#they are examples of higher order functions
#they have their own syntax, using '@'(syntax sugar)

def be_polite(fn):
    def wrapper():
        print('What a pleasure to meet you!')
        fn()
        print('Have a great day!')
    return wrapper

#we are decorating our function with politeness!
#we are 'wrapping' the above funciton in with the function below!
# def greet():
#     print('My name is Jamie.')
#this means we dont need to set what greet is!
#greet = be_polite(greet)

####-------------------------------NEW CODE----------------------------------------------####
#we can use a decorator to do the same thing as above!!.
@ be_polite
def greet():
    print('My name is Sophie')
@be_polite
def rage():
    print('I hate you!!')

#because we added the new code.. we can just call greet sratight away.. (without having to set greet)
greet()
rage()

####-------------------------------------------------------------------------------------####

##########################################
#Functions with different signatures
##########################################

# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

####--------------------------------NEW CODE---------------------------------------------####
## with the *args and **kwargs we can make anything work with with the shout function.
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, *kwargs).upper()
    return wrapper
##this means we can add anything to shout and it doesnt matter how many args or kwargs we have it will still work.
####-------------------------------------------------------------------------------------####

@shout
def greet(name):
    return f'Hi ,im {name}'

#this wont work in the old code, see what ive added to make it work. (it has two arguments, the wrapper in shout only has 1 arguments.)
@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side or {side} please."

greet('Jamie')
order('Steak', 'Fries')


##########################################
#Using wraps to preserve metadata
##########################################

# def log_function_data(fn):
#     def wrapper(*args, **kwargs):
#         '''I AM A WRAPPER FUNCTION'''
#         print(f'You are about to call {fn.__name__}')
#         print(f'Here is the documentation: {fn.__doc__}')
#         return fn(*args, **kwargs)
#     return wrapper
# @log_function_data
# def add(x,y):
#     '''Adds two numbers together'''
#     return x+y
# add(3,4)
#
# add.__doc__ #wont work properly it will just come up with the wrapper documentation

from functools import wraps
def log_function_data(fn):
    ####--------------------------------NEW CODE---------------------------------------------####
    @wraps(fn) #this will let us keep the '__doc__' for add and also be able to call 'help()'' on it as well.
    ####-------------------------------------------------------------------------------------####
    def wrapper(*args, **kwargs):
        '''I AM A WRAPPER FUNCTION'''
        print(f'You are about to call {fn.__name__}')
        print(f'Here is the documentation: {fn.__doc__}')
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    '''Adds two numbers together'''
    return x+y
add(3,4)

add.__doc__ #now this will work and come up with 'Adds two numbers together' not the wrapper doc.
#########################################
#notice how we have the @wraps
from functools import wraps
#wraps preserves a functions metadata when it is decorated
def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #do something with fn(*args, **kwargs)
        pass
    return wrapper

##########################################
#More useful ways of using decorators
##########################################
# Let's define a speed_test decorator (notes will be added later.)
from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}") #with 'wraps' we can access the name of what function we are using and it wont come up with 'speed_test'
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums_gen():
	return sum(x for x in range(90000000))

@speed_test
def sum_nums_list():
	return sum([x for x in range(90000000)])


print(sum_nums_gen())
print(sum_nums_list())

##########################################
#no kwargs function
from functools import wraps

def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed! sorry :(") #will error if any **kwargs are set
		return fn(*args, **kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print(f"hi there {name}")

greet(name="Tony")#this wont work because we have set a **kwargs by settin the name to Tony
greet('Tony') #this works because we have just called greet with Tony in the brackets, not setting a **kwargs
