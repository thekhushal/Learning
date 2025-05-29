-- SELECT EVERYTHING
SELECT * FROM world.city;
-- SELECT SPECIFIC FIELDS/COLUMNS
SELECT Name, CountryCode FROM world.city;
-- SELECT ALL CITIES FROM AUSTRALIA
SELECT * FROM world.city WHERE CountryCode = "AUS";
SELECT * FROM world.city WHERE CountryCode IN ("AUS", "USA");
SELECT * FROM world.city WHERE CountryCode LIKE "A%A";
SELECT * FROM world.city WHERE Population <= 1000;
SELECT * FROM world.city WHERE CountryCode IN ("AUS", "USA") AND Population <= 100000;
SELECT * FROM world.city WHERE CountryCode IN ("AUS", "USA") OR Population <= 100000;
SELECT COUNT(*) AS CNT FROM world.city WHERE CountryCode IN ("USA");
 