package com.linkedList;

import java.util.LinkedList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        LinkedList<String> WaitingLine = new LinkedList<>();

        WaitingLine.addAll(List.of("Rahul", "Aman", "Priya"));

        WaitingLine.addLast("Neha");

        WaitingLine.addFirst("Vikram");

        WaitingLine.removeFirst();

        WaitingLine.remove("Aman");

        WaitingLine.add(1, "Riya");

        System.out.println(WaitingLine);

        System.out.println(WaitingLine.getFirst());

        System.out.println(WaitingLine.getLast());

        System.out.println(WaitingLine.size());
    }
}
/*
Add "Neha" to the end of the line.
Add "Vikram" to the front of the line.
Remove the person at the front of the line.
Remove "Aman" from the list.
Add "Riya" at index 1.
Print the final list.
Print the person currently at the front.
Print the person currently at the end.
Print the number of people in the line.
*/