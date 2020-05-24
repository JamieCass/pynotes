#######################################################################
# Iterators and Generators
#######################################################################

##########################################
#
##########################################











##########################################
# Custom For Loop
##########################################
#Ill go through this and make comments when tomorrow!!!
# for num in [1,2,3]
# for char in "hi there"

def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)

def square(x):
	print(x*x)

my_for("lol", print)
my_for([1,2,3,4,5], square)

##########################################
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration




for x in Counter(50,70):
	print(x)
