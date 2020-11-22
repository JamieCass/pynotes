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

#Encapsulate - pretty much means break it down into smaller parts.
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
		self.first = first #this is setting the first name attribute to 'Joe' for user 1 and 'blanca' for user 2.
		self.last = last  #same as above but for the last name.
		self.age = age  #again the same thing as above.

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

#instance method is pretty much adding a funciton/method into your class, after youve done your __init__.
#these are individual pretty much

#A good example is below, with the full_name and initials functions. (always have self as first parameter)

#To call the instances we just use .instance. again a good example is below.


# A User class with both instance attributes and instance methods
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.likes("Ice Cream")) # 'Joe likes Ice Cream'
print(user2.likes("Chips")) # 'Blanca likes Chips'

print(user2.initials()) # 'J.S'
print(user1.initials()) # 'B.L'

print(user2.is_senior()) # False
print(user1.age) #Print age before we update it
print(user1.birthday()) #updates age wjile saying happy birthday
print(user1.age) #Print new value of age


#e.g of a bank account (basic of course)

# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num
        
    def withdraw(self,num):
        self.balance -= num

jamie_acct = BankAccount('Jamie') #add an account for me..
jamie_acct.owner #Jamie
jamie_acct.balance #0.0
jamie_acct.deposit(10) #10.0
jamie_acct.withdraw(6) #4.0
jamie_acct.balance #4.0


#Or like this.. breaking it down a bit more

class BankAccount:
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance




##########################################
# Introducing class attributes
##########################################

#Usually write it at the top of the class and is only defined once.

#Its good to keep track of things. like in the active users example.
#Its also good for validations.

#A class attribute is shared by all instances of a class and by the class itself.

#e.g

# A User class with both a class attribute
class User:

	active_users = 0 #we define what active users is.. 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1 #we add 1 every time __init__ is called (everytime someone logs on/or creates a user.)

	def logout(self): #when we use the logout it will take 1 away from active users.
		User.active_users -= 1 
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.initials())
# print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# user1.say_hi()

print(User.active_users) # 0
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users)# 2 (because we ran the user 1 and user 2 makine 2 active users)
print(user2.logout()) # we will make thi user log out.
print(User.active_users) # 1 



# Another class with a class attribute, used for validation purposes
class Pet:

	#Its good to have this up here if you use it more than once.. weve used it in both functions.

	allowed = ['cat', 'dog', 'fish', 'rat'] #we are setting what animals are allowed as pets

	def __init__(self, name, species):
		if species not in Pet.allowed: #if the species isnt in the allowed then it will print an Error message.
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	#This bit of code will stop people setting a species to anything not allwed in the 'allowed list'
	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")



#Chicken coop exercise

class Chicken:

    total_eggs = 0
   
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs +=1
        return self.eggs


c1 = Chicken(name='Sophie', species='Patridge Silkie')
c2 = Chicken(name='Jamie', species='Speckled Sussex')
Chicken.total_eggs #0
c1.lay_egg() #1
Chicken.total_eggs #1
c2.lay_egg()#1
c2.lay_egg()#2
Chicken.total_eggs #3





#################################################################
#Difference between Class method and Class Attribute
#################################################################

## METHOD: A 'FUNCTION' stored in an instance or class (not used a lot) 

## ATTRIBUTE: A 'VARIABLE' stores in an instance or a class


# e.g (stackoverflow)

a = 10                          # variable

def f(b):                       # function  
    return b ** 2

class C:

    c = 20                      # class attribute

    def __init__(self, d):      # "dunder" method
        self.d = d              # instance attribute

    def show(self):             # instance method
        print(self.c, self.d) 

e = C(30)
e.g = 40   





##########################################
#Class method (starts with '@classmethod')
##########################################

#Not commonly used.
#Not really concerned with instances but the class itself.

#e.g using the same Users info we did earlier

# A User class with both instance attributes and instance methods
class User:
	active_users = 0

	#Class method to print out how many active users there are.
	@classmethod
	def display_active_users(cls): #typical to use ('cls'), just like __init__ uses ('self')
		return f"There are currently {cls.active_users} active users"

	#More of a realistic class methoid and something more useful
	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",") #telling us what each value is in the string then split it on the comma.
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"



# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users()) #'There are currently 2 active users'
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users()) #'There are currently 4 active users'


#This is for the useful class method 

tom = User.from_string("Tom,Jones,89") #Helpful for sorting csv data like this and adding a new user.
print(tom.first) #Tom
print(tom.full_name()) #Tom Jones
print(tom.birthday()) #Happy 90th birthday




##########################################
#The __repr__ method
##########################################

#One of several ways to provide a nicer string representation.


class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	# NEW CODE
	def __repr__(self):
		return f"{self.first} is {self.age}"
	# NEW CODE

	#so if i now print a user it will tell you their age as well.


	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


tom = User.from_string("Tom,Jones,89")

j = User("judy", "steele", 18)
j = str(j)
print(j)


