package com.hashSet;

import java.util.HashSet;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        HashSet<Integer> a = new HashSet<>(List.of(10, 20, 10, 30, 40, 20, 50, 30));
        
        System.out.println(a);

        System.out.println(a.size());

        System.out.println(a.contains(30));

        System.out.println(a.contains(99));

        a.remove(20);
        
        System.out.println(a);


    }
}
/*
Use a HashSet<Integer> to:

    Add all the numbers.
    Print the resulting set.
    Print how many unique numbers there are.
    Check whether 30 exists.
    Check whether 99 exists.
    Remove 20.
    Print the final set.
*/