import java.util.Scanner;
public class c_Hands_on{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        if ((num % 5) == 0) {
            System.out.println("The Number is divisible by 5");
        }
        sc.close();
    }
}

/*
Hands-On Exercise 3

Ask the user for a number.

If the number is divisible by 5, print:

The number is divisible by 5.
*/