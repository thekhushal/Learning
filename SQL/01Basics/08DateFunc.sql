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

























