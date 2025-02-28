-- ---------
-- Functions
-- ---------

-- Block of code => code resuable
-- code redable
-- pre-defined function

-- --------------------
-- string function
-- --------------------


select first_name, lower(first_name), upper(lower(first_name)) from actor;
-- Here 'lower' is a function 
-- it can also be nested as we did in the third feild

select first_name, last_name,
concat(first_name, '-', last_name),
concat_ws('-', first_name, last_name)
from actor;
-- Here we are using 'concat' to combine all the parameters in it
-- if we dont add '-' or any seprator there will be no seprator

-- Concat_ws here the first parameter is the seprator, and this seprator will be automatically applied between all the parameters given to concat_ws

-- usecase
-- say you need to pull details of a person named ED CHASE (First name and last name are together)

select * from actor
where concat(first_name, ' ', last_name) = 'ED CHASE';


-- NOTE - Indexing for string starts from 1st index unlike 0th in python

-- SubStr
select first_name, 
substr(first_name, 2), 
-- here a sub string is returned starting from 2nd index

substr(first_name, 1,1),
-- returns the firt character iof the string

substr(first_name, 1,3),
-- here a sub string of length 3 is returened starting from 1st index

substr(first_name, -3) 
-- we can also work with negative indexing in sql
-- here characters from third last character to last character are printed
from actor; 

-- instr

select first_name, 
instr(first_name, 'e') 
from actor;
-- instr returns the index of mentioned character 
-- it starts iterating from 1st index and returns the index of character when finds it
-- even if the character is present multiple times in string, index of their first occurance is returned
-- if the character is not present, zero is returned (remember theres no 0th index in sql)

-- char length
select first_name, char_length(first_name)
from actor;

-- dual table

select 'hey', 'hello' from dual;

-- Diff between length and char length
select length('漢'), char_length('漢') from dual;

-- lpad

select first_name, 
lpad(first_name, 3, '!') 
from actor;
-- paarameters of lpad
	-- 1st => feild name or value we want to pass
    -- 2nd => minimum length it should be
    -- 3rd => character that should be added to left if it is not of desired length
-- lpad is used when we want a character to a at any minimum length
-- if the character if not of that minimum length lpad adds the character we have specifid to the left

-- trim

select '    dual     ',
trim('    dual     ') from dual;

select 'Trim', 
trim(leading 'z' from 'zzzSQLzzz'),
-- Output => 'SQLzzz'
-- Using this syntax we can trim desired character from the begining of the string

trim(trailing 'z' from 'zzzSQLzzz'),
-- Output => 'zzzSQL'
-- Using this syntax we can trim desired character from the ending of the string

trim(both 'z' from 'zzzSQLzzz')
-- Output => 'SQL'
-- This syntax is used to trim desired character from both starting and ending of the string

from dual;


-- Replace
SELECT first_name, REPLACE(first_name, 'E','A') FROM actor;

-- Round
select 12345.12345, round(12345.12345, 2) from dual;
-- output => 12345.12
select 12345.12345, round(12345.12345, 1) from dual;
-- output => 12345.1
select 12345.12345, round(987654321.12345, -3) from dual;
-- output => 987654000




