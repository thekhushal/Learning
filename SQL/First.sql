-- get those amount where the total number of payments for the amount should be greater then the total payment of amount 0.99

select amount, count(amount) from payment
group by amount
having count(amount)> (select count(amount)
                        from payment
                        where amount = 0.99)


-- Multi-Row subquery
-- if you have a subquery that returns more than one row/column or something than we cannot use operators like = < > etc.

-- Operators for Multi-Row
-- 'in'
-- 'any'
    -- = < > are also used with any
    -- eg where amount >any (Multi-Row sub query)
    -- if > is used with any, amounts more than smallest returned value of multi-row subquery is returned

-- get each coustomer id and the total amount spend where the total amount should be greater than the total amount spended by coustomer id 9

select * form payment

-- Learning Assignment

-- what is co-related subquery
-- what is data base 
-- what is DBMS
-- Types of DBMS with example
-- DBMS vs RDBMS
-- difference b/w where and having
-- what is sql and what are sql languages
-- what are keys
    -- primary key with eg
    -- candidate key with eg
    -- super key with eg






