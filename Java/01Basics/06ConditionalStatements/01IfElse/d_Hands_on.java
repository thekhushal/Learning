import java.util.Scanner;
public class d_Hands_on {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your marks: ");
        int marks = sc.nextInt();

        if (marks >= 90){
            System.out.println("A");
        } else if (marks >= 80){
            System.out.println("B");
        } else if (marks >= 70){
            System.out.println("C");
        } else if (marks >= 60){
            System.out.println("D");
        } else {
            System.out.println("F");
        }
        sc.close();
    }
}
