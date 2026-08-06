package com.code.b;

public class Circle {

    // Instance variable (attribute)
    double radius;

    // Constructor
    Circle(double radius) {
        this.radius = radius;
    }

    // Methods (behaviors)
    double area() {
        return Math.PI * radius * radius;
    }

    double circumference() {
        return 2 * Math.PI * radius;
    }

    void display() {
        System.out.println("Radius: " + radius);
        System.out.println("Area: " + area());
        System.out.println("Circumference: " + circumference());
    }
}
