#######################################################################
# Testing with python
#######################################################################

##########################################   OBJECTIVES   ##########################################

# Describe what tests are wand why they are essential
# Explain what Test Driven Development is
# Test python code using doctests
# Test python using assert
# Explain what unit testing is
# Write unit tests using the unittest module

##########################################   WHY TEST?   ##########################################

# Reduce bugs in existing code
# Ensure bugs that are fixed stay fixed
# Ensure that new features dont break old ones
# Ensure that cleaining up code doesnt introduce new bugs
# Makes development more fun!

##########################################   TEST DRIVEN DEVEOPMENT   ##########################################

# Development begins by writing tests
# Once tests are written, write code to make tests pass
# Once tests pass, a feature is considered complete

#--------------- RED, GREEN, REFACTOR ---------------

# RED - Write a test that fails

# GREEN - Write the minimal amount of code necessary to make the pass

# REFACTOR - Clean up the code, while ensuring that tests still pass.

##########################################   ASSERTIONS   ##########################################

# We can make simple assertions with the 'assert' keyword
# 'assert' accepts an expression
# Returns 'none' if the expression is truthy
# Raises an 'AssertionError' if expression is falsy
# Accepts an optional error message as a second argument
# AssertionError will be raised if the assert isnt true
# If a python file is rane with the '-O' flag, assertions are ignored!!!!
#e.g
def add_positive_numbers(x,y):
    assert x > 0 and y > 0, 'Both numbers must be positive!' #if both numbers arent positive, this message will come up.
    return x + y
add_positive_numbers(1,-1)

#e.g
def eat_junk(food):
    assert food in [
    'pizza',
    'ice cream',
    'candy',
    'doughnuts'
    ], 'food must be a junk food!'
    return f'NOM NOM I am eating {food}'

food = input('ENTER A FOOD PLEASE:')
eat_junk(food)

##########################################   DOCTESTS   ##########################################

# We can write tests for functions inside of the docstring
# Write code that looks likes its inside of the REPL

# REPL looking code e.g
def add(x,y):
    '''add together x and y

    >>> add(1, 2)
    3

    >>> add(8, 'hi')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    '''
# The '>>>' show how the user should use the function and what should happen if an Error was to occur

# another example
def add(a, b):
    '''
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    '''
    return a * b

add(4,5)
## to run this in through commandline without calling the function we can just type this in:
# python3 -m doctest -v (filename) --- this will test what we put in the docstring

#------- if you ran the above code with the add function we wrote, it will look something like this...

#Trying:
#   add(2, 3)
#Expecting:
#   5
#**************************************************
#File 'filelocation for the file youre testing'
#Failed example:
#   add(2 ,3)
#Expected:
#   5
#Got:
#   6      and then carry on with trying the next example in the docstring we made
#**************************************************
#1 items had failures:
#   2 of  2 in 'filename'
#2 tests in 2 items
#0 passed and 2 failed
#***Test Failed*** 2 failues.


#---------- Issues with doctests ----------
# Syntax is a little strange
# Clusters up our function code
# Lacks many features of larger testing tools
# Tests can be brittle

##########################################   UNITTESTS   ##########################################

# Test smallest parts of an application in isolation(e.g units)
# Good candidates for unit testing: individual classes, modules or functions
# Bad candidates for unit testing: an entire application, dependencies across several classes or modules.

# Python comes with a built in module called unittest
# You can write unit tests encapsulated as classes that inherit from 'unittest.TestCase'
# This inheritance gives you access to many assertion helpers that let you test the behaviour of your functions
# You can run the tests by calling 'unittest.main()'
# To see comments, run 'python3 NAME_OF_TEST_FILE.py -v'
#important to set all the tests in activities and the functions in there, to make sure test will pass. otherwise all tests below will fail.

import unittest

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
    	"""eat should have a positive message for healthy eating"""
    	self.assertEqual(
			eat("broccoli", is_healthy=True),#this is the condition, if it passes then the line bellow will also be printed
			"I'm eating broccoli, because my body is a temple"
    	)
    def test_eat_unhealthy(self):
    	"""eat should indicate you've given up for eating unhealthy"""
    	self.assertEqual(
			eat("pizza", is_healthy=False),
			"I'm eating pizza, because YOLO!"
    	)
    def test_eat_healthy_boolean(self):
    	"""is_healthy must be a bool"""
    	with self.assertRaises(ValueError):#raises a ValueError if is_healthy is not a booleen!
    		eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
    	"""short naps should be refreshing"""
    	self.assertEqual(
    		nap(1),
    		"I'm feeling refreshed after my 1 hour nap"
    	)
    def test_long_nap(self):
    	"""long naps should be discouraging"""
    	self.assertEqual(
    		nap(3), "Ugh I overslept.  I didn't mean to nap for 3 hours!"
    	)
    def test_is_funny_tim(self):
    	self.assertEqual(is_funny("tim"), False)
    	# self.assertFalse(is_funny("tim"), "tim should not be funny")

    def test_is_funny_anyone_else(self):
    	"""anyone else but tim should be funny"""
    	self.assertTrue(is_funny("blue"), "blue should be funny")
    	self.assertTrue(is_funny("tammy"), "tammy should be funny")
    	self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
    	"""laugh returns a laughing string"""
    	self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

if __name__ == "__main__":
    unittest.main()

##########################################   BEFORE AND AFTER HOOKS   ##########################################
# setUp and tearDown
# For larger applications, you may want similar application state before running tests
# setUp rund before each test method
# tearDown runbs after each test method
# Common use casses: adding/removing data from a test database, creating instances of a class.

class SomeTest(unittest.TestCase):
    # this is how you would write a setUp and tearDown test

    def setUp(self): # This will run before any of the code below.
        # setup code goes here!
        pass

    def test_first(self):
        # setUp runs before this test
        # tearDown will run after
        pass

    def test_second(self):
        # setUp runs before this test
        # tearDown will run after
        pass
        
    def tearDown(self): # This will run after each test function.
        # teardwon code goes here
        pass
