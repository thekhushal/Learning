-- create database regex;
-- use regex;
-- create table product( pid int, pname varchar(20), price int);
-- insert into product values(10,"Iphone",20000), (11,"TV",10000),
-- (12,"LED",3000), (13,"Jeans",800);

-- select * from product;

-- create table orders1( oid int, city varchar(20), pid int);
-- insert into orders1 values(124111,"Jaipur",10), (124112,"GOA",11),
-- (145631,"Manali",12), (59869011,"Raipur",16);
-- select * from orders1;


-- -- cross join or cartisian jion
-- 	-- every row of first tabel will join with every row of second table 
-- 	-- so when we do not give a condition in a join statement, a cartisian join is formed
-- select 
-- 	o.id, o.city, o.pid, p.name, p.pid 
-- from orders1 as o join product as p;

-- -- common condition
-- select 
-- 	o.id, o.city, o.pid, p.name, p.pid 
-- from orders1 as o join product as p where o.pid = p.pid;

-- -- new syntax, Inner join
-- select
-- 	oid, o.city, o.pid, pname, p.pid 
-- from orders1 as o 
-- INNER join product as p 
-- where o.pid = p.pid;

-- -- Types of join
-- -- Left Join, Right Join, Inner Join, Full outer JOin
-- -- NOTE - SQL does not support full outer join, others languaces like oracal does, but mysql doesnot

-- -- LEFT JOIN
-- select
-- 	oid, o.city, o.pid,
--     pname, p.pid 
-- from orders1 as o 
-- LEFT join product as p 
-- on o.pid = p.pid;
-- -- we do not use where condition with left join


-- -- ---------------------------------------------
-- use sakila;
-- select * from actor;
-- select * from film_actor;
-- select * from film;

-- -- you have to comibine film actor and film table to find the actor id film id and movie name done by each actor
-- select fa.film_id, fa.actor_id, f.title
-- from film_actor as fa 
-- join film as f 
-- where fa.film_id = f.film_id;

-- -- findout the actor id the movie name only for those movies which has a length of more than 100
-- select fa.actor_id, f.title
-- from film_actor as fa 
-- join film as f 
-- where f.length > 100 ;

-- -- get the actor id and the number of movies he has done in his carier
-- select actor_id, count(film_id) 
-- from film_actor group by actor_id;

-- -- get the title and the film id for the movies with rating of NC-17 and sort all these movies based on decending order of film id
-- select film_id, title
-- from film 
-- where rating = 'NC-17'
-- order by film_id desc;


slect * from actor 