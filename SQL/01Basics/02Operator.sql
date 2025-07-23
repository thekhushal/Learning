-- operators
	-- Arithmetic Operator
		-- (+, -, *, /, %)
        
	-- Comparision Operator
		-- (<, >, <=, >=, =, (!= and <>))
		-- != and <> both are not equal in sql
		-- unlike '==' in python '=' is used in sql
    
    -- Logical Operator
		-- AND, OR, NOT
	
    -- Assignment Operator
		-- equal to '='
        -- unlike python where'==' is used in sql '=' is used as assignment operator
    
	-- Set Operator
		-- UNION, UNION ALL, INTERSECT, INTERSECT
		
    -- Bit Wise Operator
		-- (&, `, ^, ~, <<, >>)
        
	-- Special Operator
		-- (BETWEEN, LIKE, NOT LIKE, IN, NOT IN, IS NULL, IS NOT NULL, EXISTS, ANY/SOME, ALL)
	
-- Combining two Operators
	-- Between ... and   (Checks if a value is in a given range (inclusive))
	select * from customer where customer_id between 5 and 25;

-- Operator Precedence
	-- From highest to lowest:
	-- 1. () — Parentheses
	-- 2. *, /, % — Multiplication, Division, Modulus
	-- 3. +, - — Addition, Subtraction
	-- 4. Comparison: =, !=, >, <, >=, <=
	-- 5. NOT
	-- 6. AND
	-- 7. OR    

    -- Example 1
		-- Case 1
			select * from customer where not active = 1 and store_id = 1 ;
			-- the command above is interpreted as the command bellow with parenthesis
			select * from customer WHERE (NOT (active = 1)) AND (store_id = 1);
			-- This means store id should be 1 and active should not be 1
		-- Case 2
			SELECT * FROM customer 
			WHERE NOT (active = 1 AND store_id = 1);
			-- Return customers who are not both active and from store 1.
	-- Example 2
		SELECT * FROM customer
		WHERE store_id = 2 OR active = 0 AND last_name = 'DAVIS';
		-- What SQL sees (because AND has higher precedence than OR):
        SELECT * FROM customer WHERE store_id = 2 OR (active = 0 AND last_name = 'DAVIS');


-- Trying all the operators
select customer_id, 
customer_id + 1 as "+ 1",
customer_id - 1 as "- 1",
customer_id * 5 as "* 5",
customer_id / 10 as '/ 10',
customer_id % 3 as "% 3"
from customer;


select 
customer_id as 'AllCustomerId\'s',
customer_id > 10 as MoreThan10,
customer_id < 10 as LessThan10,
customer_id >= 10 as '>=10', 
customer_id <= 10 as '<=10',
customer_id = 10 as EqualTo10
from customer;
