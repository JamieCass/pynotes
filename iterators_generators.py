#######################################################################
# Iterators
#######################################################################

##########################################
 # Iterators and Iterable (looping pretty much)
##########################################
#Iterator-- an object tha can be iterated on (returns data one element at a time when next() is called on it)
#When next() is called on an iterator it will return the next item and will keep going until it raises a StopIteration error.

#Iterable-- an object that will retrn an Iterator when iter() is called on it.


'HELLO' #is iterable
iter('HELLO') #returns an iterator

#e.g
name = 'Sophie'
it = iter(name) #need to put it into an iterator object.
next(it) #'S'     #we can now use nect on 'it' to go through it one at a time until it doesnt have anything to go over anymore.
next(it) #'o'
next(it) #'p'
next(it) #'h'
next(it) #'i'
next(it) #'e'
next(it) # StopIteration Error message
#so next runs through it one by one until there are no more objects in the list/string then it will gve the error message

##########################################
# Custom For Loop
##########################################
# for num in [1,2,3]
# for char in "hi there"

def my_for(iterable, func):
    #we need to make sure we run iter on whatever we put into my_for so we can run the next() function on it.
	iterator = iter(iterable)
	while True:
        #this try statement will keep running next on whatever (iterator) is.
		try:
			thing = next(iterator)
        #this will make sure the error message isnt printed when you run through the string or list.
        #the except statement will stop the try statement if it hits the error message, then it will break the loop.
		except StopIteration:
			break
        #this will make sure it prints or does whatever the func you defined in the function at the start.
		else:
			func(thing)

#we create a square function, and we can now use this as our func in my_for.
def square(x):
	print(x*x)

my_for("lol", print)
my_for([1,2,3,4,5], square)

##########################################
# Custom Iterator
##########################################
#our version of the range() function.
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high
	#need to make we define what iterator is in Counter
	def __iter__(self):
		return self
	#need to define the behaviour of next
	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for x in Counter(50,70):
	print(x)


##########################################
# Making our Deck class iterable
##########################################
from random import shuffle

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:

    def __init__(self):
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['Spades','Clubs','Hearts','Diamonds']
        self.cards = [Card(value,suit) for value in values for suit in suits]

    def __repr__(self):
        return f'Deck of {self.count()} cards

	#this code will let us iterate over all cards in the deck, using a for loop or list comp.
	#-----------NEW CODE-----------
	def __iter__(self):
		return iter(self.cards)
	#-----------NEW CODE-----------

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,num):
        return self._deal(num)
    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full deck can be shuffled')
        shuffle(self.cards)
        return self


#######################################################################
# Generators
#######################################################################

#still iterators
#shorter way of creating interators
#can be created with generator functions
#generator functions use the yeild keyword
#genertaors can be created with generator expressions

#Functions 				--- uses return	| returns onces				| when invoked, returns the return value
#Generator functions 	--- uses yield	| can yield multiple times	| when invoked, returns a generator

#e.g the same as the counter class, but a lot smaller!!! (its a generator)
def count_up_to(max):
	count = 1
	while count <= max:
		# this wont return anything other than 'generator object ......' so its turned it into a generator
		yield count
		count +=1

count_up_to(5) #returns 'generator obect ..... etc ........'
counter = count_up_to(5)
counter # still print out the same thing
next(counter) #1
next(counter) #2 and so on.
#so yield stops at the last object and then forgets whatever was before it. only stores 1 thing at a time.

#e.g 2
def week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day

#e.g dont really get this one, but it was a task on the course.
#a generator that returns 'yes' then 'no' then 'yes' and so on.
def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        answer = 'no' if answer == 'yes' else 'yes' #dont really get this line..

gen = yes_or_no()
next(gen) #yes
next(gen) #no
next(gen) #yes
next(gen) #no ..... and so on blah blah
next(gen)


##########################################
# Making a beat Generator
##########################################
# Lame function that returns a list of beats.
# Only runs 100 times
def current_beat():
	max = 100
	nums = (1,2,3,4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0
		result.append(nums[i])
		i += 1
	return result

# Infinite Generator - returns one beat a time, no list used!
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

##########################################
#function that takes a count of a drink and returns a generator with verses from a song

'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(verses = 99, drink = 'soda'):
	for num in range(verses, -1, -1):
		if num > 1:
			yield '{} bottles of {} on the wall.'.format(num, drink)
		elif num == 1:
			yield 'Only 1 bottle of {} left!'.format(drink)
		else:
			yield 'No more {}!'.format(drink)

song = make_song(8, 'Morgans spiced')
next(song)
next(song)

##########################################
#Testing memory usage with Genertaors
##########################################
# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(max):
     nums = []
     a, b = 0, 1
     while len(nums) < max:
         nums.append(b)
         a, b = b, a+b
     return nums

fib_list(10)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


for n in fib_gen(10):
	print(n)

##########################################
#Testing speed
##########################################

import time

# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time() # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time # end time - start time


# SUMMING 10,000,000 Digits With List Comprehension
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")
