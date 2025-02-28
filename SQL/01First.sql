show databases;
-- The command above is used to list all the databases we have

use sakila;
-- This command is used to start using a particular database

show tables;
-- This command lists all the tables in the database we are using

desc actor;
desc actor_info;
-- "desc" is used to describe a table in the database
-- It gives a breif description of the database

select * from actor;
-- This statement selects everything from the actor table 
-- "*" is used when you want to select everything from the database

select actor_id, first_name from actor;
-- insted of "*" we can also put name of the feilds(columns) we wish select

select actor_id, first_name, ACTOR_ID, LaSt_NamE FROM actor;
-- SQL is not a case sensitive language
-- Data is case sensitive but not the statements
-- use upper case or lower case where ever you wish

-- same feild can be displayed multiple times like we displayed actor_id multiple  times


select actor_id, first_name, actor_id*100 from actor;
-- here when we multiplied a felid by 100, all the records (rows) in that feild were multiplied 100
-- also the name of the felid was displayed as it was in the query

-- this does not change anything in the actual database, database remanis the same, change is only applied here.






