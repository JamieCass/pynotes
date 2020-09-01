#######################################################################
# SQL with Python
#######################################################################
##########################################
 # Connecting to a DB with Python and INSERTING
##########################################
import sqlite3

# create a new database (my_friends.db) that we will store the information into. or connect to a DB if theres already one there.
conn = sqlite3.connect('my_friends.db')

#----- create cursor object -----
c = conn.cursor() # this will allow us to execute commands

#----- execute some sql -----

#create a new table
#c.execute('CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)') #make a new table with this information in.

#insert into the table a new friend
insert_query = '''INSERT INTO friends
                    VALUES ('James', 'Rover', 6)'''
c.execute(insert_query)

#----- commit changes -----
conn.commit()
# we have to close the connection after we have finished.
conn.close()
