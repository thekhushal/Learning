use sakila;

-- Where Clause
select * from actor
	where actor_id = 2;
-- This is where clause, it is used to apply conditions to filter data

-- Having Clause
select store_id, count(*) as total_customers
from customer
group by store_id
having count(*) > 10;
-- This is having clause, it is used to apply conditions to the group by result

-- Where vs Having
	-- Where is used to filter rows before grouping, while Having is used to filter groups after grouping.
	-- Where cannot be used with aggregate functions, while Having can be used with aggregate functions.
	