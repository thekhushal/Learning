SELECT * FROM world.city;
SELECT Name FROM world.city;
SELECT Name FROM world.city where population >= 100000;
SELECT Name, CountryCode, Population FROM world.city where Population >= 100000;
SELECT Name, CountryCode, Population FROM world.city where Population >= 100000 and CountryCode Like "S%";
SELECT Name, CountryCode FROM world.city WHERE CountryCode LIKE "A%A";