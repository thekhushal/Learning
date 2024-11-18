select * from world.city;
SELECT * from world.city order by Population, CountryCode desc;
SELECT * from world.city where CountryCode like "%T" or CountryCode like "P%" order by Population, CountryCode desc;
select count(*) from world.city where ID >= 4000 and CountryCOde = "USA" order by name;
select * from world.city where District like "R%" and CountryCode = "IND";
select count(*) from world.city where District like "G%" and CountryCode = "IND";
select count(distinct population) from world.city;
select count(distinct District) from world.city ;
-- what if i wnat distinct district but with everything else
select * from world.city where CountryCode = "USA" and District = "A%" ;
