-- Orfer by,  alias, multi  row function 

use sakila;
-- ------------------------
-- Ordder by
select * from actor order by first_name, actor_id desc;
-- -----------------------
-- alias
select actor_id, actor_id + 10 as new_actor_id from actor;
-- -----------------------

-- multi row function
-- Functions that are applied to multiple(or all) rows of any column
select * from payment;

select distinct(customer_id) from payment;
select count(customer_id) as Total_Customers from payment;
select count(distinct(customer_id)) as Unique_Customer from payment;

select 
	count(customer_id) as Total_Customers,
	count(distinct(customer_id)) as Unique_Customer,
    count(customer_id) - count(distinct(customer_id)) as repetitive_customer 
from payment;

select
	count(amount),
    sum(amount),
    avg(amount),
    max(amount),
    min(amount)
from payment;

-- Note - all these functions skip null values BUT count function dosent, count function even counts null values
    
-- Aggrigate functions are the functions which are used to perform operatons over multiple values to result in one value

-- with an aggrigate function you cannot select a normal function.
	-- for example 
    -- select sum(amount), amount, payment_id, from payment;
		-- this query is incorrect as here we attempt to select an agrigate function with a normal row
        -- sql wouldnt know where to show sum(ammount) and with which row sould we show it