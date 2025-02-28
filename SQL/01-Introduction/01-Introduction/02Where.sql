use sakila;

-- Where Clause
select * from actor
	where actor_id = 2;
-- This is where clause, it is used to apply conditions to filter data

select * from actor
	where actor_id between 1 and 5;
	-- When using between 1 and 5 is legal but 5 and 1 is not

select * from actor
	where actor_id in (2, 10, 50, 500);
    -- When using in only mentioned valuse will be given
    -- if a value out of scope is listed it will be ignored no error will be returned like 500 in thi scase
    
select actor_id, first_name from actor
	where first_name in ('NICK', 'ED');
    
select actor_id, first_name from actor
	where first_name = 'NICK' or first_name = 'ED';
    
-- LIKE Operator
	-- WildCard Character
		-- '%' => zero or more character
        -- '_' => only one character
	-- Suppose you wish to find all names starting from 'E' you cannot so it with '=', we use like for it

select * from actor
	where first_name like 'E%';
    -- Here we got all first names starting with 'E'

select * from actor 
	where first_name like '%y';
    -- Here we got all first names ending with 'y'
    
select * from actor
	where first_name like 's%y';
    -- Here we got all first names starting with 's' and ending 'y'
 
 -- If you wish to pull all the First names that consist of character 'a'
 select * from actor
	where first_name like '%a%';
    
    

select * from actor
	where first_name like 'E_';
    
select * from actor
	where first_name like '_A';
    
select * from actor
	where first_name like '_A%';
    
