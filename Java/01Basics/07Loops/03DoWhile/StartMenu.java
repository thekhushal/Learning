import java.util.Scanner;
public class StartMenu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 1;
        do {
            if (i < 1 || i > 2){
                System.out.println("==========Option not found!==========");
                System.out.print("Do you wanna see the menu again: (y/n)");
                sc.nextLine();
                String check = sc.nextLine();
                if (check.equals("n")) {
                    break;
                }else if (check.equals("y")){
                    // the do while continues from here
                }else{
                    System.out.println("Choose from here");
                }
            }
            System.out.println("----------Menu----------");
            System.out.println("1. Re-load menu \n2. Exit");
            System.out.print("Kindly Pick an option:");
            i = sc.nextInt();
            // System.out.println();
        }while(i != 2);

        sc.close();
    }
}
