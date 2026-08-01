public class Recursion {

    // Prints numbers from n to 0
    static void printNumbers(int n) {

        // Base Case
        if (n == 0)
            return;

        System.out.println(n);

        // Recursive Call
        printNumbers(n - 1);
    }

    // Print factorial of n 
    static int factorial(int n) {

        // Base Case
        if (n == 1)
            return 1;

        // Recursive Case
        return n * factorial(n - 1);
    }

    // print sum of all numbers up till n
    static int sum(int n) {

        if (n == 0)
            return 0;

        return n + sum(n - 1);
    }

    // print numbers
    static void print(int n){
        if (n == 0){
            return;
        }

        // System.out.println(n);
        print(n-1);
        int[] lit = new int[6];
        lit[n] = n;
        if 
        
    }

    public static void main(String[] args){
        // Prints numbers from n to 0
        // printNumbers(5);

        // Print factorial of n 
        // factorial(5);

        // print sum of all numbers up till n
        // sum(5);

        // printing numbers
        print(5);
    }
}
