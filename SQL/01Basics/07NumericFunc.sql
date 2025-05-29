-- numeric functions

use sakila;

-- Single row category functions
select first_name, substr(first_name, 2) from actor; 
-- This is single row category function, this is called a single row category function because this is applied to every row 


-- numeric function
-- round, turncate, mod, pow

-- Round
select 34.35, round(24.25) from dual;
-- output => 24
select 12345.12345, round(12345.12345, 2) from dual;
-- output => 12345.12
select 12345.12345, round(12345.12345, 1) from dual;
-- output => 12345.1
select 12345.12345, round(987654321.12345, -3) from dual;
-- output => 987654000

-- round off to nearest 100
select round (24.25, -2) from dual;
-- round off to nearest 10
select round (24.77, -1) from dual;


-- truncate
select truncate(12345.12789, 2);
-- output => 12345.12
select truncate(12345.16789, 1);
-- output => 12345.1
select truncate(12345.12345, 3);
-- output => 12345.1234

select truncate(56789, -3);

-- mod
select mod(20, 2) from dual;
-- output => 0
select mod(23, 5) from dual;
-- output => 3

select 21%2 from dual;
-- output => 1

-- mod function is same as %

-- pow, floor, ceil

select pow(2, 3), floor(10.99999), ceil(2.00001) from dual;
	