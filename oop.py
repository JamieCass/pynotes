#######################################################################
# Object Oriented Programming
#######################################################################

# Not python specific
# Its a method of programming that attempts to model/represent some process or thing in the world as a class or object.

#Useful for structuring and organizing your code.



##########################################
# Class / Object
##########################################

#Class - blueprint for objects, can contain methods and attributes (similar to keys in a dict)
#Instance - pbjects that are contructed from class blueprints that contain their class's methods and properties.

#When naming a class, everyone usually starts the name with a capital and end with a pass.

#e.g.
class User:
	pass

#e.g. 2 

class Vehicle:
	pass

car = Vehicle()
boat = Vehicle()




##########################################
# Abstraction and Encapsulation
##########################################

#Encapsulate - pretty much means break it down into smaller arts.
#'the grouping of public and private attributes and methods into progammatic class making abstaction possible'


#The goal is to encapsulate your code into logical,heirarchical groupings using classes.
#No need for it if theres not a lot of seperate class's


#If you wanted to make a private class you usually put an underscore '_' at the start.


#For a poker game, we would break it down (encapsulate) into seperate classes:


#Game, Player, Card, Deck, Hand, Chip, Bet.


#Lets encapsulate the deck:


#deck {class}

# _class		{private list attruibute} (can stay inside the deck)
#_max_cards		{private int attribute} (can stay inside the deck)
#shuffle		{public method} 
#deal_card		{public method}
#deal_hand		{public method}
#count 			{public method}


#e.g

#Designing the Deck class, make the cards a private attribute (a list)

#The length of cards should be accessed via a public mathod called count() -- i.e. Deck.count()


#Abstraction - exposing only 'relevent' data in a class interface, hiding private attributes and method ('inner workings') from users. 



##########################################
# the __init__ method
##########################################

#Everytime we make a class python we need to define the __init__ method unless there no data in the class (rare).



#Always have to have self at the beginning of __init__. "def __init__(self):"

#Self keyword refers to the current class instance.

#Technically it doesnt have to be called self but its standard and its pretty much the only thing you will see.
#self pretty much calls the instance. so below its just caling user then we define first and second and so on in brackets.



# A User class with 3 attributes but no methods (aside from __init__)
class User:
	def __init__(self, first, last, age):
		self.first = first #this is setting the first name attribute to 'Joe' for ser 1 and 'blanca' for user 2.
		self.last = last  #same as above but for the last name.
		self.age = age  #again the same this as above.

user1 = User("Joe","Smith", 68)
user2 = User("Blanca", "Lopez", 41)

#when we want to print it, we have to print what we've called it in the self section.
#so it will be first, last, age. (all 3 are in called from self.first, last, or age.)

print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)



# e.g. 2 

class Vehicle:

	def __init__ (self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

#creating an object that is an instance of a class is called INSTANTIATING a class.

# e.g. 

v = Vehicle('Honda','Civic', 2017)


# v becomes a Honda Civic, a new instance of Vehicle and would look something like this...

# v
# <__main__.Vehicle at 0x10472f5c0>
# v.make
# 'Honda'
# v.model
# 'Civic'
# v.year
# 2017





##########################################
# Underscore: Dunder methods, Name Mangling.
##########################################

#The difference in the underscores and what theyre good for.

#_name (a way to tell other coders that it should be a private function/class, method or so on)
#__name (name mangling) (wont be able to access it outside!)
#__name__ (dunder)..(only use these if you want to reference/override something already in python)



#e.g.

# _name
# __name
# __name__


class Person:
	# Init is a "dunder" method
    def __init__(self):
        self.name = "Tony"
        # single underscore means "private" (sort of)
        self._secret = "hi!"
        # two leading underscores tells Python to "mangle" the name
        self.__msg = "I like turtles!"
        self.__lol = "HAHAHAHAH"


p = Person()

print(p.name)
print(p._secret) #Anyone can still directly access the attribute

print(dir(p)) # Notice what __msg and __lol have been "mangled" to

print(p._Person__msg) #this is the only way t print the mangled text!
print(p._Person__lol)




##########################################
# Adding instance methods
##########################################


