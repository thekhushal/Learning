-- Find all the rare animals and sort the query output by feeding time (from small to large)
select * from animal 
where acategory = 'rare'
order by timetofeed;

-- Find the animal names and categories for animals related to a tiger (hint: use the LIKE operator)
select aname, acategory from animal
where aname like '%tiger%';

-- Find the names of the animals that are related to the bear and are common
select * from animal
where aname like '%bear%' and acategory = 'common';

-- Find the names of the animals that are not related to the bea
select * from animal
where aname not like '%bea%';

-- List the animals (animal names) and the ID of the zoo keeper assigned to them.
select * from animal; 

-- Now repeat the previous query and make sure that the animals without an assigned handler also appear in the answer.

-- Report, for every zoo keeper name, the minimum number of hours they spend feeding an animal in their care.

-- Report every handling assignment (as a list of assignment date, zoo keeper name and animal name). 
-- Sort the result of the query by the assignment date in an ascending order.