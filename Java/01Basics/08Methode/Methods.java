public class Methods {
    // method to print line
    static void printline(){
        System.out.println("--------------------");
    }

    // method to print a message
    static void welcome(){
        System.out.println("Welcome to Java");
    }

    // method to multiply two numbers
    static void product(int a, int b){
        System.out.println(a*b);
    }

    // method to welcome user
    static void bio(String name, int age){
        System.out.println("My name is " + name + " and i am " + age + " years old.");
    }

    // returning product
    static int multiply(int a, int b){
        return a*b;
    }

    // returning after computation
    static boolean isAdult(int age){
        if (age >= 18 ){
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args) {
        // to Print the "Welcome to java bannar"
        printline();
        welcome();
        printline();

        // Multiplying two numbers using method
        product(3, 5);
        printline();

        // bio
        bio("khushal", 22);
        printline();

        // returning product
        int a;
        a = multiply(5,7);
        System.out.println(a);

        // 
        boolean b = isAdult(9);
        System.out.println(b);

    }
}
