import pyfiglet
from termcolor import colored
#make a tuple with all allowed colors in termcolor
allowed_colors = ('red','green','yellow','blue','magenta','cyan','white')


# msg = input('What would you like to say? ')

# color = input('What color do you want? ')
# #set a default color if input is invalid.
# if color not in allowed_colors:
#     color = 'green'


# #make the message look dfferent using the figlet.format
# ascii_art = pyfiglet.figlet_format(msg)

# #make the ascii art come out a set color

# colors_ascii = colored(ascii_art, color = color)

# print(colors_ascii)

#####################

#make it into a function

def print_art(msg,color):
	if color not in allowed_colors:
    	color = 'green'
    ascii_art = pyfiglet.figlet_format(msg)
    colors_ascii = colored(ascii_art, color = color)
	print(colors_ascii)

msg = input('What would you like to say? ')
color = input('What color do you want? ')
print_art(msg,color)