-- Date Function

-- Bellow are functions for current Date, Time, Date and time together respectively
select curdate(), curtime(), now(), current_timestamp() from dual;
-- now() and current_timestamp() are same

-- adddate() function
select curdate(), adddate(curdate(), 1);
-- this add one day to result

select curdate(), adddate(curdate(), interval 1 month);
-- this adds a month to result

select curdate(), adddate(curdate(), interval 1 year);
-- this adds a year to result

select curdate(), adddate(curdate(), interval 1 week);
-- this adds a WEEK to result

select curdate(), adddate(curdate(), interval -1 year);
-- this SUBTRACTS a year to result



-- DATEDIFF

SELECT datediff('2025-05-16', '2026-05-16') from dual;

-- last day of month

select last_day( now() ) from dual;
select last_day(now()) from dual;



-- ----------------------------
-- 
select 
	month( now() ), 
	year ( now() ) 
from dual;


-- EXTRACT - month 
select extract( year from now() ) from dual;


-- -----------------------

-- fate function 
-- capital M gives may
-- lower m gives 05
select now(), date_format(now(), 'this year is %Y');
select now(), date_format(now(), 'this year is %Y');


-- curdate()
-- curtime()
-- current_timestamp()
-- now()
-- adddate(now(), 20), adddate(NOw(), interval 2 hours)
-- year(), month(), weelofyear(), date()
-- extract(year from now()), extract (month from now())
-- date_format(noe(), 'Year is %Y, %y, %M, %t')
	-- here %y %y %M %t all mean different, go tho the documentation to check what each mean
-- datediff()

-- where, like, in, between
-- and or not
-- functions, string func, number func, date func
-- aggregate functions (multi row functions) max min avg sum
-- with the where clause you can only use data thats already in the table, aggregate functions cannot be used with where clause
	-- select customer_id, sum(amount) from payment where sum(amount) group by customer_id; this is wrong as due to the reasom above, use having in this query
-- i need to get that particular customer ,and the amount spend in the month of june where the total payment excede amount 50
-- select customer_id, amount from payment where month(payment_date) = 06 group by customer_id havig sum(amount) > 50

-- get the avg aomunt spended in each month by the stock
-- diff between where and having clause
-- distinct vs group by
-- what is sql and type of sql langusges


-- what are relationships 














