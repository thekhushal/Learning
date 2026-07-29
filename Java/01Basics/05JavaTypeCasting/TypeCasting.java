import java.util.Scanner;

public class TypeCasting {
    public static void main(String[] args) {
        System.out.print("Enter a Decimal point number: ");
        Scanner sc = new Scanner(System.in);
        double num = sc.nextDouble();

        System.out.println("Original Value: " + num);

        int intnum = (int) num;

        System.out.println("After Casting to int " + intnum );

        sc.close();
    }
}
