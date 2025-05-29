use sakila;
select * from actor;
-- if Function
-- syntax => if (condition, if true, if false)
select first_name, actor_id, 
	if (first_name = 'NICK', 'Hello NICK', 'its not nick')
    from actor;
    
-- nested if function

select first_name, actor_id, 
	if (first_name = 'NICK', 'Hello NICK', if (first_name = 'ED', 'Hello ED', 'who are you'))
    from actor;
    
-- if actor id is even, first name and last name should concat, else concat with a $ symbol

select actor_id, 
	if( actor_id%2 = 0, concat(first_name, last_name), concat(first_name, '$', last_name) )
    from actor;
    
-- case

select first_name, 
case 
	when actor_id % 2 = 0 then concat (first_name, ' ', last_name)
    else concat (first_name, '$', last_name)
end
from actor;
