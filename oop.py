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

#Wehn naming a class, everyone usually starts the name with a capital and end with a pass.

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

#If you wanted to make a private class you usually put a '_' at the start.

#For a poker game, we would break it down (encapsulate) into seperate classes:

#Game, Player, Card, Deck, Hand, Chip, Bet.

#Lets encapsulate the deck:

#deck {class}

# _class		{private list attruibute} (can stay inside the deck)
#_max_cards		{private int attribute} (can stay inside the deck)
#shuffle		{public method} ()
#deal_card		{public method}
#deal_hand		{public method}
#count 			{public method}

#e.g

#Designing the Deck class, make the cards a private attribute (a list)

#The length of cards should be accessed via a public mathod called count() -- i.e. Deck.count()


#Abstraction - exposing only 'relevent' data in a class interface, hiding private attributes and method ('inner workings') from users. 










