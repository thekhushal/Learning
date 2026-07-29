import java.util.Scanner;

public class a_Hands_On {
    public static void main(String[] args) {
        System.out.print("Enter your age: ");
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt();

        if (age >= 18){
            System.out.println("You are elegible to vote for BJP");
        }

        sc.close();
    }
}
/*
Hands-On Exercise 1

Write a program that:
Asks the user for their age.
If the age is 18 or above, print:
You are eligible to vote.
Otherwise, print nothing.
*/