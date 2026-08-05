package com.code.a;

class Test{
    static String name;
    
    // Constructor
    public Test(String name){
        Test.name = name;
    }
}

public class Accessing_Top_level_Class {
    public static void main(String[] args) {
        Test t = new Test("Khushal");
        Test b = new Test("sharma");

        System.out.println("Accessing Static Attribute via object: "+t.name);
        System.out.println("Accessing another static attribute or class variable via object and getting a warning as it should be accessed via class"+(b.name));
        System.out.println("Accessing class Attribute via class: "+ Test.name);
    }
}
