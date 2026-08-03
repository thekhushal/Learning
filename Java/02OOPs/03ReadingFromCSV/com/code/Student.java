package com.code;

public class Student{
        int rno;
        String name;
        double marks;

        Student(int rno, String name){
            this.rno = rno;
            this.name = name;
        }
        Student(int rno, String name, double marks){
            this.rno = rno;
            this.name = name;
            this.marks = marks;
        }
        Student(){
            rno = 0;
            name = "Default";
            marks = 0.0;
        }
    
}