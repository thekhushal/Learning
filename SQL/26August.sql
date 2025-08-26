create table studentacess; -- ddl

create table StudentAcess(id int, sname varchar(10));

insert into studentacess (id,sname) values(21, "aman");
insert into studentacess (id,sname) values(24, "naina");

select * from studentacess;

delete from StudentAcess;

/*
-- merge do not work in mysql but does work in some other languages
merge into targettable as t
using sourcetable as s
on t.id = s.id
when matched then
		expression
when not matched then 
		expression
when not matched by source then
		delete;
        
        or

mrege into table using referance_table
when contition then statement (insert/update/delete)
*/

-- truncate helps you retain the structure of the table by just deleting the data of the table not the table structure
truncate table studentacess;

-- truncate vs delete
	-- truncate deletes the entire table ----> and then recreates the structure of the table
    

create table test18 (id tinyint);
insert into test18 values (10);
insert into test18 values (-128);
insert into test18 values (-129); -- didnt work because tinyint will have a size range from -128 to 127 a total of 256 intigers
insert into test18 values (127);
insert into test18 values (128);
select * from test18;


