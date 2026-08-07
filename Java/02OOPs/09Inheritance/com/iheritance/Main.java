package com.iheritance;

class Programer extends Employee{
    String department;
    int level;
    double bonus;

    Programer(int id, String name, double salary, String department, int level, double bonus){
        super(id, name, salary);
        this.department = department;
        this.level = level;
        this.bonus = bonus;
    }
}

class Employee{
    int id;
    String name;
    double salary;
    
    public Employee(int id, String name, double salary){
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

}

class Display{
    public void id(int o){
        System.out.println(o);
    }

    public void out(Object... args){
        for (Object arg : args){
            System.out.println("\t" + arg);
        }
    }
}
public class Main {
    public static void main(String[] args) {
        Programer p1 = new Programer(1, "Khushal", 1200000.00, "BackEnd Development", 1, 30000.00);
        Programer p2 = new Programer(2, "Rahul", 500000000, null, 0, 0);

        Display display = new Display();

        display.id(p1.id);
        display.out(p1.name, p1.salary, p1.department, p1.level, p1.bonus);

        display.id(p2.id);
        display.out(p2.name, p2.salary, p2.department, p2.level, p2.bonus);
    }
}
