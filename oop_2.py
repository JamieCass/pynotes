#######################################################################
# Object Oriented Programming - Part 2
#######################################################################

##########################################
# Inheritance
##########################################

#a key feature in OOP, the ability to define a class which inherits from another class (a 'base' or 'parent' class)
#admin and inherit from user..

#how to tell python you want to inherit from one class to another
#it works by passing an argument to the definition of a child class

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

	#NOT NEEDED IF WE MAKE PROPERTIES INSTEAD (MUCH NEATER)
	######################
	# def get_age(self):
	# 	return self._age

	# def set_age(self, new_age):
	# 	#make sure that age is more than 0
	# 	if new_age >= 0:
	# 		self._age = new_age
	# 	else:
	# 		self._age = 0
	#######################

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


# Its just a bit nice code that doing the whole def set_age thing.



james = Human('James', 'Cork', 54)

#need parens to call it.
print(james.get_age())

# so we can just call -- from the property that we just made. dont need parens!!
print(james.age) # 54

# now we made a setter we can change the age like this and it will change the age from 54 to 29
james.age = 29 # 29

print(james.full_name) #James Cork



##########################################
# Super() intro
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

#e.g good examply of how to inherit and use super()

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

#make a moderator class, (someone who is above the average user).
class Moderator(User): # so Moderator inhertics all Users methods.

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
		super().do_something()#This will rint out the C statement.

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

#define a chile class that uses MRO to inherit from Mother first then Father.


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





