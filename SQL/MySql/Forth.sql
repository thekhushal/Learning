-- SELECT
	-- SELECT * -- Return all column
	SELECT * FROM world.city;
	-- SELECT (Coumn(s)) -- Return Given Column(s)
	SELECT (CountryCode) FROM world.city;

	-- SELECT DISTINCT(Column(s)) -- Return given column(s) WITH distinct Rows
	SELECT DISTINCT(CountryCode) FROM world.city;

-- COUNT : It Counts no. of rows of given or all column
	-- No. of rows or cities
    SELECT COUNT(*) FROM world.city;
    SELECT COUNT(Name) FROM world.city; -- BOTH are SAME
    
    -- NO. of DISTINCT Rows in given
    SELECT COUNT(DISTINCT(Name)) FROM world.city;
	
-- MAX, MIN, SUM, AVG
	SELECT MIN(Population), MAX(Population), SUM(Population), AVG(Population) FROM world.city;

-- WHERE
	-- <, <=, >, >=, =
	-- IN
    -- LIKE
    -- AND, OR
-- ORDER BY
-- GROUP BY
-- 