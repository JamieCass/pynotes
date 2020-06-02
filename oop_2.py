#######################################################################
# Object Oriented Programming - Part 2
#######################################################################

##########################################
# Inheritance
##########################################

#a key feature in OOP, the ability to define a class which inherits from another class (a 'base' or 'parent' class)
#admin and inherit from user..
#how to tell python you want to inherit from one class to another, it works by passing an argument to the definition of a child class

#e.g
#base class
class Animal:
	def make_sound(self,sound):
	print(sound)

	cool = True

#inherit class from cat(Animal). Rather than self, we told python to inherit it from the Animal class
class cat(Animal):
	#need to pass otherwise an error will come up.
	pass

#make a cat called gandalf
gandalf = Cat()
#told it to 'meow' so it puts it into the Animal class which it 'INHERITED'
gandalf.make_sound('meow') # meow

gandalf.cool # True
#this will come up true becuase we have made gandalf the cat, which has inherited the Animal class.
print(isinstance(gandalf, Animal)) #True



##########################################
# Properties
##########################################

#pretty much just a more pythonic way to set certain and call certain things in python, best to look at example below.

#e.g
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0

	# NOT NEEDED IF WE MAKE PROPERTIES INSTEAD (MUCH NEATER)
	# #####################
	# def get_age(self):
	# 	return self._age
	#
	# def set_age(self, new_age):
	# 	#make sure that age is more than 0
	# 	if new_age >= 0:
	# 		self._age = new_age
	# 	else:
	# 		self._age = 0
	# ######################

	#decorator, set up the property age so we dont neew parethases.
	@property #(getter) property
	def age(self):
		return self._age

	#setting the property part of age.. so needs to be the same name as the property above.
	@age.setter #(setter) property
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			self._age = 0
			# or coule be an Error message..
			#raise ValueError('age cant be negative')

	#property to call the full name.
	@property
	def full_name(self):
		return f'{self.first} {self.last}'


# Its just a bit nicer code than doing the whole def set_age thing.

james = Human('James', 'Cork', 54)

#need parens to call it.
print(james.get_age())

# so we can just call -- from the property that we just made. dont need parens!!
print(james.age) # 54

# now we made a setter we can change the age like this and it will change the age from 54 to 29
james.age = 29 # 29

print(james.full_name) #James Cork



##########################################
# Super()
##########################################

#super() refers to the BASE class info so you can use it in other classes. See below
#Really useful for multiple inheritences


class Animal:
	def __init__(self, name, sepcies):
		self.name = name
		self.species = species
	def __repr__(self):
		return f'{self.name} is a {self.species}'

	def make_sound(self,sound):
	print(f'This animal says {sound}')


class Cat(Animal):
	def __init__(self, name, breed, toy):

		#------- HOW SUPER IS USED --------
		#its pulling the ifo from Animal so you dont have to specify whar selfname or species is anymore.
		super().__init__(name, species = 'Cat')


		#------- Another longer way to do what super does ---------
		Animal.__init__(self, name, species) #could do this inseatd of below.

		#-------Dont waste your time keep re-writing everything. Just use super()
		#self.name = name #should already have this from the Animal class
		#self.species = species #should already have this from the Animal class
		self.breed = breed
		self.toy = toy

	def play(self):
		return f'{self.name} likes to play with {self.toy}'

blue = Cat ('Blue', 'Pursian', 'Rat')
print(blue) #Blue is a Cat
print(blue.species) #Cat
print(blue.breed) #Pursian
print(blue.toy) #Rat
print(blue.play) #Blue likes to play with Rat


#e.g good example of how to inherit and use super()
class User:

	#we define what active users is.. 0
	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		#we add 1 every time __init__ is called (everytime someone logs on/or creates a user.)
		User.active_users += 1

	#when we use the logout it will take 1 away from active users.
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

#make a moderator class, (someone who is above the average user).
# so Moderator inherits all Users methods.
class Moderator(User):

	def__init__(self, first, last, age, community):
		#pulling the info (first, last, age) from User class using super()
		super().__init__(first, last, age)
		self.community = community

	def remove_post(self):
		return f'{self.full_name} removed a post from the {self.community}'

jasmine = moderator('Jamsmine', 'Platt', 22, 'Gaming')
print(jasmine.full_name) #Jasmine Platt
print(jasmine.community) #Gaming


########### -- RPG Character set up -- ############

#make a character that has cert name hp and level
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

#Non-Player-Character that we want to inherits from Character but also says something with a speak method.
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return {}.format(self)

#You can also define what class to inherit from in the super() brackets.


##########################################
# Method Resolution Order (MRO)
##########################################

#Whenever you create a class python sets a MRO for that class.
#its the order in which python will look for methods on instances of that class.

#you can see the MRO for a class in three different ways.

__mro__ #attribute on the class
mro() #method on the class
help(cls) #built in method (probably the best one)

#e.g for multiple inheritence and MRO


	#		A       (A)  Base class
	# 	  /   \
	#	 B     C    (B and C)  both inherit from A
	#	  \   /
	#		D       (D)  inherits from B and C
	#D,B,C,A,Object

class A:
	def do_something(self):
		print('Method defined in: A')

class B(A):
	def do_something(self):
		print('Method defined in: B')
		super().do_something()#This will print out the C statement.

class C(A):
	def do_something(self):
		print('Method defiuned in: C')

class D(B,C):
	# if we comment this out... what will come first out of B and C when calling thing.do_something()??
	def do_something(self):
		print('Method defined in: D')
		super().do_something() #This will print out the B statement, because it inherits from B first.

thing = D()

thing.do_something() #Method defined in: D

#to find out what order it will do in we can do any of the above
print(D.mro()) # main D, main B, main C, main A, object (Thats the order)


help(D) #looks like.
#------------------------------
#class D(B,C)
#	Method resolution order:
#		D
#		B
#		C
#		A
#		builtins.object
#	Methods inherited from B:
#------------------------------

#define a child class that uses MRO to inherit from Mother first then Father.
class Mother:
    def __init__(self):
        self.eye_color = 'brown'
        self.hair_color = 'dark brown'
        self.hair_type = 'curly'

class Father:
    def __init__(self):
        self.eye_color = 'blue'
        self.hair_color = 'blond'
        self.hair_type = 'straight'


class Child(Mother, Father):
    pass


########################################
#this is a bigger exapmlw. notice how penguin is both AMBULATORY and AQUATIC. so it inherits from both classes.
class Ambulatory:
  def __init__(self,name):
    print("AMBULATORY INIT!")
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"



class Penguin(Ambulatory, Aquatic):
  def __init__(self,name):
    print("PENGUIN INIT!")
    super().__init__(name=name)
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)



jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")

# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() # ??


##########################################
# Polymorphism
##########################################

#Poly(many) Morph(forms)
#A key principle in OOP is the idea of Polymorphism -an object can take on 'many' 'forms'.

#1. same class method works in a similar way for different classes, (same method name but behanving in different ways) like below eg.
#e.g of how same class method works in a different way. They all have a speak method but the print is different.
Cat.speak() # meow
Dog.speak() # woof
Human.speak() # hello

########################################
#2. same operation works for different kinds of objects.
#e.g of how len() works for a list, tuple and a string.
sample_list = [1,2,3]
sampel_tuple = (1,2,3)
sample_string = 'awesome'

len(sample_list) # 3
len(sampel_tuple) # 3
len(sample_string) # 7

########################################
# this is an example of how each class inherits from Animal and has to return a speak method otherwise you get an Error.
class Animal():
	def speak(self):
		raise NotImplementedError('Sublass needs to implement this method')

class Dog(Animal):
	def(self):
		return 'woof'

class Cat(Animal):
	def(self):
		return 'meow'

#this one wont work becase we havent returned a speak method.
class Fish(Animal):
	pass


########################################
class Aquatic:
  def __init__(self,name):
    print("AQUATIC INIT!")
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"

a = Aquatic('Jamie')
a.swim()
##########################################
# Special __magic__ methods
##########################################

#Magic methods are basically Dunder methods.
#good eg of this is the + operator.. behing the scenes its a special method called __add__()
8 + 2 # 10 --- if the first operand is a instance of int, __add__() does mathematical addition
'8' + '2' # 82 --- if its a string the __add__() does string concatenation

# little example of how we can make our own version of __len__ to return the height of a human.
class Human:
	def __init__(self, height):
		self.height = height # in inches

	def __len__(self):
		return self.height
Jamie = Human(73)
len(Jamie) # 73

##########################################
#here's anther example of using the special methods in a better Human class
from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def __repr__(self):
		return f'Human named: {self.first} {self.last}'

	def __len__(self):
		return self.age

	#Make a baby??!! by using the __add__ so wehn we do human '+' human,  neworn will be made.
	def __add__(self, other):
		#do a little check to make sure that other is Human.
		if isinstance(other, Human):
			return Human(first = 'Newborn', last = self.last, age = 0)
		return 'You cant add that!'

	def __mul__(self, other):
		#multiply Human by the int, so we get a copy of that human.
		if isinstance(other, int):
			#we use the copy function, this will return a copy of the human we input.
			return [copy(self) for i in range (other)]
		return 'CANT MULTIPLY'


j = Human('Jenny', 'Furgo', 45)
k = Human('George', 'Hassy', 44)
j+k # this is using the __add__ method we made in the Human class.
j*3 # this will create a copy of the human j by using the __mul__ method we made in the Human class.
(k+j) * 3 # we can also multiply babies by adding k and j then multiplying it by whatever int we want.

##########################################
#GrumpyDict exercise
#we inherit from the dict class already made by python.
class GrumpyDict(dict):
	def __repr__(self):
		#print this
		print('None of your business')
		#this will return whatever is in the GrumpyDict class repr (which is standard for what the python class will show.)
		return super().__repr__()
	#this will come up when the GrumpyDict is missing a key.
	def __missing__(self, key):
		print(f'You want {key}? WELL IT AINT HERE')
	#we use this if we want to add a key and value to a dict
	def __setitem__(self, key, value):
		print('Yo want to change the dictionary?')
		print('OK FINE...')
		#we need this to make the change actually happen. calling from the python function setitem
		super().__setitem__(key, value)

data = GrumpyDict({'First': 'Tom', 'Animal':'Dog'})
#this will bring up the message that there isnt a key called city in the dict we are looking in.
data['city']
#so if we want to add a city then we can do it now, because we made the __setitem__ function.
data['city'] = 'London'
data['Animal']
