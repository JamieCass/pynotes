#######################################################################
# File I/O
#######################################################################

##########################################   OBJECTIVES   ##########################################

# Read text files in Python
# Write text files in Python
# Use 'with' blocks when readin / writing files
# Describe the different ways to open a file
# Read CSV files in Python
# Write CSV files in Python

##########################################   READING FILES   ##########################################

# You can read a file wiht the 'open' function
# 'open' returns a file pbject to us
# You can read a file object with the 'read' method
# CHECK THE DOCUMENTATION FOR MORE INFO

# e.g
file = open('story.txt')
file.read()

######################   CURSOR MOVEMENT   ######################

# Python reads files by using a cursor
# This is like the cursor you see while youre typing
# After the file is read, the cursor is at the end of the file
# To move the cursor, we use the 'seek' method
# The connection between the we are reading and this file are always open until we close it!
# Its important to close/stop the connection when youve finished with it

# seek(0) will put the cursor back to the start
file.seek(0)

# this will read the first line and stop after it reaches the '\n'
file.readline()

# this will read all the lines and put them in a list of seperate strings.
file.readlines()

#--------------- CLOSING A FILE ---------------
# You can close a file with the 'close' method
# You can check if a file is closed with the closed attribute
# Once closed, a file cant be read again. (unless you re-open it)

# to close the file
file.close()

# to check if the file is closed or not (will return True/False)
file.closed

######################   WITH BLOCKS   ######################

# Option 1
file = open('story.txt')
file.read()
file.close()

# Option 2 (this closes the file automatically, and it looks neater)
with open('story.txt') as file:
    data = file.read()

file.closed
data

##########################################   WRITING TO FILES   ##########################################

# You can also use 'open' to write to a file
# Need to specify the 'w' flag as the second argument

# e.g
with open('haiku.txt', 'w') as file:
    file.write('Writing to the file \n')
    file.write('Here is another line \n')
    file.write('Ok goodbye!\n')

# if you dont have a file, with the code below i have just made a new file called lol.
# the code below has made a new file called lol.txt
with open('lol.txt', 'w') as file:
    file.write('LOL ' * 1000)

##########################################   FILE MODES   ##########################################

# 'r' open for reading (default)
# 'w' open for writing, truncating the file first (will create a new file if there isnt one.)
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the 'end' of the file if it exists (will create a new file if there isnt one.)
# 'b' binary mode
# 't' text mode (default)
# '+' open for updating (reading and writing)
# 'r+' read and write to a file (writing based on cursor)

# this will start from the beginning, we havent said where we are going to start the cursor
with open('haiku.txt', 'r+') as file:
    file.seek(100)
    file.write('Just adding this new line in for the example\n')

##########################################   NEW TASK   ##########################################
# Write a function called copy, which takes ina  file name and a new file name and copies the contents of the first file to the second file

def copy(file_name, new_file_name):
    #first open the first file and use the read() method and save the it as text
    with open(file_name) as file:
        text = file.read()

    #second open the new file with the 'w' saying we want to write into the file
    with open(new_file_name, "w") as new_file:
        #now we just write into the new file with all the contents we read from the first file
        new_file.write(text)

##########################################   NEW TASK   ##########################################
# Write a function called copy_and_reverse, which takes a file name and a new file name and copies the reversed contents of the first tile to the second file.

def copy_and_reverse(file, new_file):
    with open(file) as file1:
        text = file1.read()
    with open(new_file, 'w') as file2:
        file2.write(text[::-1])

##########################################   NEW TASK   ##########################################
# Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words and characters in the file.

def statistics(file):
    with open(file) as f:
        data = f.read()
        lines = len(data.splitlines())
        chars = len(data)
        words = len(data.split())

        return {'lines': lines,
                'words': words,
                'characters': chars,}
statistics('story.txt')

# COULD OF DONE IT LIKE THIS (its a bit easier and looks nicer)
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

##########################################   NEW TASK   ##########################################
# Write a function which takes a file name,  a word to search for and a replacement word. Replaces all instances of the word in the file with the replacement word.

'''
find_and_replace('story.txt', 'Alice', 'Colt')
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''
with open('story.txt', 'w') as f:
    f.write('Jamies story\nIm going to write a bit in here and try and change the name Jamie.\nIf I can change the name, I would of don\'t the task.')

def find_and_replace(file, word, new_word):
    with open(file, 'r+') as f:
        data = f.read()
        new_text = data.replace(word, new_word)
        f.seek(0)
        f.write(new_text)
find_and_replace('story.txt', 'Jamie', 'Sophie')
