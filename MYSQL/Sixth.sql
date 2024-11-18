SELECT * FROM world.city;
-- Get a list of all countries with no. of cities and total population 
-- SELECT CountryCode ,COUNT(*) AS "NO. of Cities", SUM(Population) AS Population FROM world.city GROUP BY CountryCode;
SELECT * FROM world.city group by CountryCode;
-- Get a list of 
-- SELECT CountryCode FROM world.city GROUP BY CountryCode liKe "A%";
-- Get a list of countries with their population , Highest populated country in order of highest to lowest
SELECT CountryCode, SUM(Population) AS Population FROM world.city GROUP BY CountryCode order by Population desc;
-- Give the highest populated city and its population 
SELECT CountryCode, Name, Population FROM world.city GROUP BY CountryCode, Name, Population;
SELECT * FROM world.country;
SELECT * FROM world.city;

-- Joining multiple tables
-- List all columns
SELECT * FROM world.city ct JOIN world.country cu ON ct.CountryCode = cu.Code;
-- List specific columns
SELECT ID, District, Continent FROM world.city ct JOIN world.country cu ON ct.CountryCode = cu.Code;
-- List specific columns including common column names
SELECT ID, ct.Name AS City, District, cu.Name AS Country, Continent FROM world.city ct JOIN world.country cu ON ct.CountryCode = cu.Code;
-- List all coumns from a specific table and select columns from other table
SELECT ct.*, cu.Name AS Country, Continent FROM world.city ct INNER JOIN world.country cu ON ct.CountryCode = cu.Code;
/*
TC1	TC2
1	3
2	2
3   4
5   1
1   6

INNER JOIN => common results (intersection)
LEFT JOIN => Everything from left table, with join on right wherever possible
RIGHT JOIN => Everything from right table, with join on left wherever possible
OUTER JOIN => Everything from both tables, with joins wherever possible


*/