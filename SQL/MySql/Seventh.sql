CREATE DATABASE MnB;
CREATE TABLE MNB.Product (
    PRDID int NOT NULL auto_increment,
    Name varchar(100),
    Category varchar(100),
	PRIMARY KEY (PRDID)
);

CREATE TABLE MNB.Employee (
	EMPID int NOT NULL auto_increment,
    Name varchar(100) NOT NULL,
    Address varchar(100),
    City varchar(100),
    MobileNO varchar(10),
    Designation	varchar(100),
    Salary int,
    Headquarter varchar(100),
	ManagerID int,
    PRIMARY KEY (EMPID),
    FOREIGN KEY (ManagerID) REFERENCES Employee(EMPID)
);

CREATE TABLE MNB.Sale (
	SaleID int not null auto_increment,
    Date varchar(100) not null,
    EMPID	int not null,
    PRDID	int not null,
    Amount int not null,
    PRIMARY KEY (SaleID),
    FOREIGN KEY (EMPID) REFERENCES Employee(EMPID),
    FOREIGN KEY (PRDID) REFERENCES Product(PRDID)
);

insert into MNB.employee (Name, Address, City, MobileNO, Designation, Salary, Headquarter, ManagerID) values ("Alpha2", "CHA", "Harayana", "21345", "State Head", 300000, "Chandigarh", "2");
insert into MNB.employee (Name, Address, City, MobileNO, Designation, Salary, Headquarter, ManagerID) values ("Beta22", "HIS", "Hisar", "315345", "Region Head", 100000, "Hisar", "5");
insert into MNB.employee (Name, Address, City, MobileNO, Designation, Salary, Headquarter, ManagerID) values ("Gama51", "CHA", "CHANDIGARH", "614345", "City Head", 50000, "CHANDIGARH", "12");
insert into MNB.employee (Name, Address, City, MobileNO, Designation, Salary, Headquarter, ManagerID) values ("Gama61", "HIS", "HISAR", "754345", "City Head", 50000, "HISAR", "12");
insert into MNB.employee (Name, Address, City, MobileNO, Designation, Salary, Headquarter, ManagerID) values ("Gama62", "SIR", "SIRSA", "7545", "City Head", 50000, "SIRSA", "12");
select * from mnb.employee;

insert into mnb.product (Name, Category) value ("Kookies", "FMCG");
insert into mnb.product (Name, Category) value ("Face Wash", "Health Care");
select * from mnb.product;

Delete from mnb.employee where EMPID = 6;
update mnb.employee set ManagerID = "13" where EMPID = 20;

select * from mnb.employee;
select * from mnb.product;
select * from mnb.sale;

select * from mnb.employee;
-- List all employee under a manager
-- salary above 100000
-- Employee reporting to a smae manager
-- C