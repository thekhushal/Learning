package com.ArrayList;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> ages = new ArrayList<>();

        Scanner sc = new Scanner(System.in);

        System.out.print("How many ages do you want in list: ");
        int num = sc.nextInt();

        for (int i=0; i <num;i++){
            System.out.println("Enter " + Th.ordinal(i+1) + " age of the list: ");
            ages.add(sc.nextInt());
        }

        System.out.print("Here's your list of ages: ");
        System.out.println(ages);
        
        sc.close();
    }
}
