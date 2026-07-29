public class OperatorsPractice {

    public static void main(String[] args) {

        int a = 20;
        int b = 6;
        int age = 22;

        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulus: " + (a % b));

        System.out.println("Comparison: If a is greater expect true else false ->" + (a>b));
        System.out.println("Equality: if equal expect true else false ->" + (a==b));
        System.out.println("Divisibility: if divisible expect 0 else expect number greater than 0 ->" + (a%b));

        System.out.println("If age greater than or equal to 18 expect true -> "+ (age>=18));
        System.out.println("If age between 18 and 30 expect true -> " + (age >= 18 && age <= 30));
        System.out.println("If age less than 18 or more than 60 expect true -> " + (age <18 || age > 60));
        System.out.println("Is age not equal to 22 -> " + (age != 22));
    }
}