import java.util.Scanner;
public class b_Hands_on{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your marks: ");
        int marks = sc.nextInt();

        if (marks >= 40) {
            System.out.println("Damnnn... nigga you passed");
        }
        sc.close();
    }
}

/*
Hands-On Exercise 2

Ask the user for their marks.
If marks are 40 or more, print:
Congratulations! You passed.
Otherwise, print nothing.
*/