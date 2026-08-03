package com.code;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class c {

    public static void main(String[] args) {

        // Created several objects based on the data in the csv
        ArrayList<Student> students = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader("data.csv"))) {

            br.readLine(); // Skip header

            String line;

            while ((line = br.readLine()) != null) {

                String[] values = line.split(",");

                int rno = Integer.parseInt(values[0]);
                String name = values[1];
                int marks = Integer.parseInt(values[2]);

                students.add(new Student(rno, name, marks));
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        for (Student s : students) {
            System.out.println("Rollno: " + s.rno + "\n\tName: " + s.name + "\n\tMarks: " + s.marks);
        }
    }
}