use sakila;

-- --------------------------
-- upper & lower function
select first_name, lower(first_name), upper(lower(first_name)) from actor;
-- Here 'lower' is a function 
-- it can also be nested as we did in the third feild

-- ---------------------------
-- char length function
select first_name, char_length(first_name)
from actor;

-- Diff between length and char length
select length('漢'), char_length('漢') from dual;

-- ----------------------------
-- Concat
-- Say you need to show full name of a person named ED CHASE (First name and last name together), use concat in such case

select first_name, last_name,
concat(first_name, '-', last_name),
	-- Here we are using 'concat' to combine all the parameters in it
	-- here we use '-' as a seprator between two terms
concat_ws('-', first_name, last_name)
	-- Concat_ws here the first parameter is the seprator, and this seprator will be automatically applied between all the parameters given to concat_ws
from actor;

-- -----------------------------------------------------
-- SubStr

-- Syntax of substr
	-- substr(column_name, starting position, number of characters you want)

-- NOTE -- Indexing/position starts from 1st index unlike 0th in python
-- NOTE -- In SQL you give starting index/position and total number of character, not start and ending index.
-- example
select substr('CHETA-SINGH', 5, 3) from dual;
	-- output - A-S as A is 5th char and we asked or 3 characters

select first_name, 
substr(first_name, 2), 
	-- here a sub string is returned starting from 2nd index
substr(first_name, 1,1),
	-- returns the firt character of the string
substr(first_name, 1,3),
	-- here a sub string of length 3 is returened starting from 1st index
substr(first_name, -3),
	-- we can also work with negative indexing in sql
	-- here characters from third last character to last character are printed
substr(first_name, -5, 3) 
from actor; 

-- ----------------------------------------------------------------------------
-- instr function

select first_name, 
instr(first_name, 'e') 
from actor;
-- instr returns the index of mentioned character 
-- it starts iterating from 1st index and returns the index of character when finds it
-- even if the character is present multiple times in string, index of their first occurance is returned
-- if the character is not present, zero is returned (remember theres no 0th index in sql)
-- NOTE: Theres no 0th index in sql
-- -------------------------------------------------
-- lpad and rpad function
select first_name, 
	lpad(first_name, 5, '!') 
	from actor;
-- adds '!' if  the first name is not of length 5
-- paarameters of lpad
	-- 1st => feild name or value we want to pass
    -- 2nd => minimum length it should be
    -- 3rd => character that should be added to left if it is not of desired length
-- lpad is used when we want a character to be of any minimum length
-- if the character is not of that minimum length lpad adds the character we have specifid to the left

select first_name, 
	rpad (first_name, 5, '!')
    from actor;

-- ------------------------------------------------------
-- Trim, LTRIM, RTRIM

select 
'    dual     ',
trim('    dual     '), 
LTRIM('   Hello') AS left_trimmed,
RTRIM('World   ') AS right_trimmed 
from dual;

-- ------------------------------------------------------
-- TRIM with (LEADING TRAILING BOTH)
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
-- -----------------------------------------------------

-- Replace
SELECT first_name, REPLACE(first_name, 'E','A') FROM actor;

-- -----------------------------------------------------
-- dual table

select 'hey', 'hello' from dual;

-- ------------------------------------------------------
-- Split function


