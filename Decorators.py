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
    ####--------------------------------NEW CODE---------------------------------------------####

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

print(add.__doc__ )#now this will work and come up with 'Adds two numbers together' not the wrapper doc.
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
# Let's define a speed_test decorator.
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

##########################################   NEW TASK   ##########################################
#Write a function called show_args that accepts a function and returns another function.
#before invoking the function passed on it, show_args should be responsible for printing 2 things:
#a tuple of the positional arguments and a dictionary of the keyword arguments.

'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if args and kwargs:  #this will only work if we have args AND kwargs.. the below code will work better.
            return f'Here are the args: {args}\nHere are the kwargs: {kwargs}'
    return wrapper
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1,2,3, a='hi', b='bye')

###--------------------------could of done it like this-----------------------------------####
# def show_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("Here are the args:", args)
#         print("Here are the kwargs:", kwargs)
#         return fn(*args, **kwargs)
#     return wrapper
####--------------------------------------------------------------------------------------####

##########################################   NEW TASK   ##########################################
#Write a function called double_return that accepts a function and returns another function.
#double_return should decorate a function by returning two copies of the inner functions return value inside of a list.
'''
@double_return
def add(x, y):
    return x + y

add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

@double_return
def greet(name):
    return   "Hi I'm " + name

greet('Colt')


##########################################   NEW TASK   ##########################################
#Write a function that accepts a function and returns another funtion.
#Function passed to it should only be invoked if there are fewer than 3 positional arguments passed to it.
#Otherwise, the inner function should return 'Too many arguments!'

'''
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
'''

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args):
        if len(args) < 3:
            return fn(*args)
        return 'Too many arguments!'
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all(1,6,2)


##########################################   NEW TASK   ##########################################

'''
@only_ints
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args):
        if any(x for x in args if type(x) != int):
            return 'Please only invoke with integers.'
        return fn(*args)
    return wrapper

@only_ints
def add(x, y):
    return x + y
add(1,2)
add('1','2')


##########################################   NEW TASK   ##########################################

'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') == 'admin': #use the .get to get the name of the key in **kwargs
            return fn(*args, **kwargs)
        return 'Unauthorized'
    return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin")
show_secrets(role='nobody')

##########################################

#E.G for ensuring first arg is equal to args..
# NOT WORKING CODE!
# JUST FOR DEMO PURPOSES!

# When we write:
@decorator
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator(func)


# When we write:
@decorator_with_args(arg) #we add the argument(arg)
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator_with_args(arg)(func)

##########################################

def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val: #we check if there are args in wrapper, then we make sure its equal to val
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


@ensure_first_arg_is("burrito") #this will check if the first value in fav food is burrito.
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12)) # 12
print(add_to_ten(1, 2)) # 'Invalid! First argument must be 10'

##########################################
#enforce example (the power of decorators)

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
               newargs.append( t(a)) #feel free to have more elaborated convertion (this will zip the type with the value..?)
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int) #this will make sure whats inserted is a string and an int
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)
#repeat_msg('hello', '3')
#('hello', str) ('3', int) #this will change because we we put the 'newargs' for loop in the new_func, so it will make sure the first value is a string then the second an int (it will change it itself)
#['hello', 3] this is what it will look like. its been changed because of the we used append with the types(args) bit of code.

@enforce(float, float)
def divide(a,b):
	print(a/b)
divide('1', '4') #this will work because we are making sure that both 'a' and 'b' are both floats.

##########################################   NEW TASK   ##########################################

#function that will wait to execute the function being decorated by the amount of time passed into it.
#should also print a message informing the user there will be a delat before the decorated function get ran.

'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(num):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print  (f'Waiting for {num}s before running {fn.__name__}')
            sleep(num)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return 'Hi'
say_hi()
