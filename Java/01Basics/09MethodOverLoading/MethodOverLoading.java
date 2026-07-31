public class MethodOverLoading {

    // Method Overloading: Different data type
        // Java automatically selects the corret method by looking at the datatype
    static void print(int n) {
        System.out.println(n);
    }

    static void print(String s) {
        System.out.println(s);
    }


    // Method Overloading: Different parameter list
    static void greet() {
        System.out.println("Hello");
    }

    static void greet(String name) {
        System.out.println("Hello " + name);
    }

    // What won't work: Creating a different return type
        //  As java looks at return type much later, it will throw error when it sees two method same name same parameter list etc 
    static int test() {
        return 5;
    }
    // I have to comment it out as other wise code wont work.
    // static double test() { 
    //     return 5.0;
    // }
    public static void main(String[] args) {
        // Method Overloading: Different data type
        print("Khushal");
        print(6);

        // Method Overloading: Different parameter list
        greet();
        greet("Khushal");


    }
}
