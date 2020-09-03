import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

#bad example password should never be saved/stored like this.
#query = 'CREATE TABLE users (username TEXT, password TEXT)'

u = input('Please enter your username...')
p = input('Please enter your password...')

#------------ BAD EXAMPLE ------------
 #if you type "' OR 1=1 --" as password this will get you into the account..
# query = f"SELECT * FROM users WHERE username= '{u}' AND password= '{p}'" # a user can get into an account this way
# c.execute(query)

#------------ BETTER EXAMPLE ------------
query = "SELECT * FROM users WHERE username=? AND password=?"
c.execute(query, (u,p))

result = c.fetchone()
if result:
    print('Welcome back')
else:
    print('FAILED LOGIN')


conn.commit()
conn.close()
