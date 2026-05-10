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
select a.AName, ZName
from animal as a 
join Handles as h
    on a.AID = h.AnimalID
join ZooKeeper as z 
    on h.ZooKeepID = z.ZID
; 

-- Now repeat the previous query and make sure that the animals without an assigned handler also appear in the answer.
select a.AName, ZName
from animal as a 
LEFT join Handles as h
    on a.AID = h.AnimalID
left join ZooKeeper as z 
    on h.ZooKeepID = z.ZID
; 

-- Report, for every zoo keeper name, the minimum number of hours they spend feeding an animal in their care.
SELECT z.ZName, min(a.TimeToFeed) 
FROM ZooKeeper as z 
JOIN Handles as h 
    on z.ZID = h.ZooKeepID
JOIN Animal as a 
    on h.AnimalID = a.AID
GROUP BY z.ZID;

-- Report every handling assignment (as a list of assignment date, zoo keeper name and animal name). 
SELECT z.ZName, a.AName, h.Assigned 
FROM Handles as h 
JOIN Animal as a 
    on h.AnimalID = a.AID
JOIN ZooKeeper as z 
    on h.ZooKeepID = z.ZID
;
-- Sort the result of the query by the assignment date in an ascending order.
SELECT h.Assigned, z.ZName, a.AName
FROM Handles as h 
JOIN Animal as a 
    on h.AnimalID = a.AID
JOIN ZooKeeper as z 
    on h.ZooKeepID = z.ZID
ORDER BY h.Assigned 
;