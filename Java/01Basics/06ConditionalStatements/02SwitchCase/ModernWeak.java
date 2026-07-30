import java.util.Scanner;

import javax.naming.ldap.SortResponseControl;
public class ModernWeak {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the day number of the weak: (1 to 7): ");
        int day = sc.nextInt();

        switch (day){
            case 1 -> System.err.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday");
        }
        sc.close();
    }
}
