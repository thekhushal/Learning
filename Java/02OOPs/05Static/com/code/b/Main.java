package com.code.b;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        System.out.print("Enter the Radius of Circle: ");
        Scanner sc = new Scanner(System.in);
        
        Circle c1 = new Circle(sc.nextInt());

        c1.display();
    }
}
