#######################################################################
# Built-in Modules, custom modues, external modules
#######################################################################

#Help to keep python files small
#reuse code across multiple files using mport.

#you can import in many ways.

import random
import random as rand
from random import choice, shuffle
from random import choice as i_decide
#thats just a little example of different ways you can import.


#You can import your own python files as well

import (then the name of your file)

#you can import any custom modules
#first you need to pip install any of the ones you dont have
#then its just a simple import

from termcolor import colored

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)

# this will print the text in different color and backgrond and have it blinking!.