package com.code.c;

class Dog {
    void bark() {
        System.out.println("Woof");
    }
}

public class Making_dogs_bark {
    public static void main(String[] args) {
        // this is related to Dog class
        Dog d = new Dog();
        // Main d = new Main();
        d.bark();
    }
}
