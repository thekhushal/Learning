-- constraint
-- set of rules & regulations => invalid data
-- declaration of table
use regex1;
create table employee01(id int);

insert into employee01 values(10);

insert into employee01 values(10),(20),(30),(null),(40);

select * from employee01;

create table employee01(id int);
insert into employee01 values(10),(20),(30),(null),(40);
select id,id+5 from employee01;

drop table employee02;
create table employee02(id int, salary int default 0);
insert into employee02 values(10,99),(20,100);
insert into employee02(id,salary) values(20,null);
select * from employee02;

-- primary key
drop table employee02;
create table employee02(id int primary key, salary int unique);
insert into employee02 values(10,99),(20,100);
insert into employee02 (id,salary) values(20,1002);
insert into employee02 (id,salary) values(22,null);
select * from employee02;



create table employee02(id int primary key, fname varchar(20), 
salary int,
constraint regex_emp_salary_uk unique(salary));
insert into employee02 values (10,'a',99), (20, 'a', 99);

-- You have to create a table with student name id fee college name phone number
-- id and student name will be primary fee cannot be null the college default value will be regex 
-- and phone number will be a unique constraint, 
-- and you have to give constraint name for each value
create table student(
	id int, 
    name varchar(20), 
    fees int not null, 
    college_name varchar(20) default 'regex', 
    phone_number int);
    
-- what is normalization and its types
-- what are acid properties and what are its uses
-- Read about code related sub queris


    
 