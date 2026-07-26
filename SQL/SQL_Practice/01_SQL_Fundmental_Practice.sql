use sakila;

show tables;

select * from customer;

select * from films;

select * from payment;

-- Q1
select first_name, last_name from customer;

-- Q2
select distinct rating from film;

-- Q3 Find every customer whose email is NULL.
select first_name, last_name from customer where email is NULL;

-- Q4 Display the first 15 films alphabetically.
select 
	title 
from film 
order by title
limit 15;

-- Q5 Display length ordered from longest movie to shortest.
select length 
from film
order by length desc;

-- Q6 Find all movies whose rental duration is greater than 5 days. return title and rental_duration
select 
	title, 
    rental_duration 
from film
where rental_duration > 5;	

-- Q7 Find customers living in store 1. return customer id, first_name, last_name
select 
	customer_id, 
    first_name, 
    last_name
from customer
where store_id = 1;

-- Q8 Show all payments greater than $8. Return payment_id customer_id amount. Sort by highest payment first.
select 
	payment_id,
    customer_id,
    amount
from payment
where amount > 8 
order by amount desc;

-- Q9 Return the first 10 customers whose last name starts with 'S'.
select 
	first_name, 
    last_name
from customer
where last_name like 's%'
limit 10;

-- Q10 Display every distinct rental duration available in the film table.
select distinct rental_duration
from film;

