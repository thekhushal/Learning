package com.list;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> n1 = new ArrayList<>();
        LinkedList<Integer> n2 = new LinkedList<>();

        n1.addAll(List.of(10, 20, 30));
        n2.addAll(List.of(40, 50, 60));

        processList(n1);
        processList(n2);
    }

    static void processList(List<Integer> numbers){
        numbers.add(100);
        numbers.add(1, 200);
        numbers.set(0, 999);
        numbers.remove(2);
        System.out.println(numbers);

    }
}
/*
The method should:

    Add 100 to the end.
    Add 200 at index 1.
    Replace the element at index 0 with 999.
    Remove the element at index 2.
    Print the final list.

Then in main():

    Create an ArrayList<Integer> containing 10, 20, 30.
    Create a LinkedList<Integer> containing 40, 50, 60.
    Pass both to processList().
*/