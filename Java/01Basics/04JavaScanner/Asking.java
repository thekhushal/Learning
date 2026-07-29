import java.util.Scanner;

public class Asking {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Age: ");
        int age = sc.nextInt();

        System.out.print("Enter Height: ");
        double height = sc.nextDouble();
        sc.nextLine();

        System.out.print("Enter Learning Status: ");
        String learning = sc.nextLine();
        // Boolean learning = sc.nextBoolean(); // use this its better

        System.out.println("--------Student Details--------");
        System.out.println("Name: " + name);
        System.out.println("Age: "+ age);
        System.out.println("Height: " + height);
        System.out.println("Learning Java " + learning);
        sc.close();
    }
// Write a program that asks the user for:

// Name
// Age
// Height (decimal)
// Whether they are learning Java
}