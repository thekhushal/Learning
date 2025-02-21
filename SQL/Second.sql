-- cross join or cartesian join
    -- when each row of a table is matched with each row of the other table
    -- formula for this is m * n, as 

-- Iner join 
    -- only the commons in pid and product_iid will be reflected
select p.pid, p.name, p.price, o.city
from product as p inner join orders as o
on p.pid = o.product_id
    -- older syntax same function
    -- earlier known as equie join
select p.pid, p.name, p.price, o.city
from product as p inner join orders as o
on p.pid = o.product_id

-- Left join
    -- all the values of the table at left are returned, but only the values that matches from the right table are returned
select p.pid, p.name, p.price, o.city
from product as p left join orders as o
on p.pid = o.product_id

-- right join
    -- all the values from the right table are returned, and the values matching from the left are returned
select p.pid, p.name, p.price, o.city
from product as p right join orders as o
on p.pid = o.product_id

-- non equie join
select pid, city
from product, orders 
where pid = product_id


-- natural join
    -- natural join acts as inner join if there are common columns in both tables
    -- natural join also acts as cross join if there are no common columns in tables
    -- we do not really use it
select p.pid, p.name, p.price, o.city
from product as p natural join orders as o

-- Practice these questions on hacker rank or SQLZoo