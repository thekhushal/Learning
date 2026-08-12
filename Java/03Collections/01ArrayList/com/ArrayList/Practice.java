package com.ArrayList;

import java.util.*;

public class Practice {
    public static void main(String[] args) {
        ArrayList<Integer> marks = new ArrayList<>();

        marks.addAll(List.of(75, 82, 91, 68));

        marks.add(88);

        marks.add(2, 88);

        marks.set(0, 80);

        marks.remove(3);

        System.out.println(marks);

        System.out.println(marks.size());

        System.out.println(marks.contains(91));

    }
}

/*
Add 88 to the end.
Insert 95 at index 2.
Change the mark at index 0 to 80.
Remove the mark at index 3.
Print the final list.
Print the number of marks.
Print whether the list contains 91.
*/