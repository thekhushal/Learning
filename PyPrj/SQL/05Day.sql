-- SQLite
SELECT * FROM EMPLOYEE;
SELECT * FROM DEPARTMENT;
SELECT * FROM PROJECT;
SELECT * FROM WORKS_ON;T
-- Using the company.sql database (posted in with this assignment), write the following SQL queries.


-- 1. Find the names of all employees who are directly supervised by 'Franklin T Wong' (you cannot use Franklin’s SSN in the query, you can only use the name – one reason is that SSN is sensitive information and we do not want SSN to appear in the query history log).
SELECT 
    e.Fname as EMPLOYEE,
    s.Fname as SuperVisor
FROM EMPLOYEE as e
JOIN EMPLOYEE as s 
on e.Super_Ssn = s.Ssn
WHERE s.Fname = 'Franklin' AND s.Minit = 'T' AND s.Lname = 'Wong';

-- 2. For each project, list the project name, project number, and the average hours per week (by all employees) spent on that project.
SELECT p.Pname, p.Pnumber, avg(w.Hours) 
FROM PROJECT as p 
JOIN WORKS_ON as w 
on p.Pnumber = w.Pno
GROUP BY p.Pnumber;

-- 3. For each department, retrieve the department name and the maximum salary of employees working in that department. Order the output by department number in ascending order.
SELECT 
    d.Dname, 
    max(e.Salary) as Highest_Salary
FROM DEPARTMENT as d 
JOIN EMPLOYEE as e 
on d.Dnumber = e.Dno
GROUP BY d.Dnumber
ORDER BY d.Dnumber;

-- 4. Retrieve the average salary of all male employees.
SELECT 
    avg(Salary) as Avg_male_salary
FROM EMPLOYEE
WHERE Sex = 'M';


-- 5. For each department whose average salary is greater than $45,000, retrieve the department name and the number of employees in that department.
SELECT 
    d.Dname, 
    count(e.Ssn)
FROM DEPARTMENT as d 
JOIN EMPLOYEE as e 
on d.Dnumber = e.Dno
GROUP BY d.Dnumber
HAVING avg(e.Salary) > 45000;


-- 6. Retrieve the names of employees whose salary is within $28,000 of the salary of the employee who is paid the most in the company (e.g., if the highest salary in the company is $88,000, retrieve the names of all employees that make at least $60,000.). Naturally, your query should work for any salary.
SELECT Fnam FROM EMPLOYEE
where Salary >= ((SELECT max(Salary) FROM EMPLOYEE) - 28000);

-- 7. Find all female employees using:

-- a. Plain SELECT query
SELECT Fname, sex 
FROM EMPLOYEE
WHERE Sex = 'F';
-- b. Sub-query
SELECT Fname 
FROM (SELECT * FROM EMPLOYEE WHERE sex = 'F');

-- 8. Find all employees who are not assigned to any project using a SET operation in SQL

SELECT Ssn FROM EMPLOYEE
EXCEPT
SELECT DISTINCT Essn FROM WORKS_ON;

-- SELECT * FROM EMPLOYEE
-- WHERE Ssn in (
-- SELECT Ssn FROM EMPLOYEE
-- EXCEPT
-- SELECT DISTINCT Essn FROM WORKS_ON);
