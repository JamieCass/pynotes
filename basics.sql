------------------------------------------------------------------------------------
-- SQL + Python
------------------------------------------------------------------------------------
--just type sqlite3 into terminal and it will out you into the enviroment.
--to quit out of it... control + D

------------------------------------------
-- Create table
------------------------------------------
-- --to check tables
-- .tables
-- .schema (will let you look what the command was when making the table)
-- CREATE TABLE dogs (
--     name TEXT,
--     breed TEXT,
--     age INTEGER
-- );
-- --you need to save the table otherwise it will be deleted when you exit out..
-- .open filename.db or use sqlite3 filename.db # when you quit it would have saved
--
------------------------------------------
-- to look at the data in the table
------------------------------------------
SELECT * FROM dogs(tablename); --the * means select all
SELECT name FROM dogs; --will bring up all data in the name section of the table
SELECT name, age FROM dogs; --will bring upp all the names and ages, you see how it works.

------------------------------------------
-- ADD into a table
------------------------------------------
INSERT INTO dogs (name, breed, age) VALUES ('Poppy', 'Bishon Frise', 4);
--make sureyou follow the order you insert the info e.g(name, breed, age)
-- you can insert multiple values by running the file in the terminal with whatever info is in there.

-- lets add a couple of dogs into the dog table.
INSERT INTO dogs(name, breed, age) VALUES('Scruffy', 'Jack Russel', 16);
INSERT INTO dogs(name, breed, age) VALUES('Jet', 'Greyhound', 7);
INSERT INTO dogs(name, breed, age) VALUES('Rupert', 'Schnauzer', 4);

--to put all of these into the table type this in termainal

--sqlite3 dogs.db
--.read basics.sql (or whatever filename you have the info you want to insert into the table)
INSERT INTO dogs(name, breed, age) VALUES('Norb', 'Lab', 10);
INSERT INTO dogs(name, breed, age) VALUES('Frank', 'French Bulldog', 8);
INSERT INTO dogs(name, breed, age) VALUES('Suzie', 'Poodle', 3);

----------------------------------------
-- SELECTING
----------------------------------------
-- to select a dog by its name
SELECT * FROM dogs WHERE name IS "Scruffy";

-- to select all dogs that are Jack Russel
SELECT * FROM dogs WHERE breed IS "Jack Russel";
-- to get just their names
SELECT name FROM dogs WHERE breed IS 'Jack Russel';

-- select dogs that aren,t the breed Lab or Greyhound
SELECT * FROM dogs WHERE breed IS NOT 'Lab' AND breed IS NOT 'Greyhound';

-- select dogs that are ove a certain age
SELECT * FROM dogs WHERE age > 4;

-- select any dogs that have 'gg' in their name
SELECT * FROM dogs WHERE name LIKE "%gg%";
