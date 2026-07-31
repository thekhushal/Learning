public class Practice {
    static void display(){
        // No Argument
    }
    static void display(int age){
        System.out.println(age);
    }
    static void display(String name){
        System.out.println(name);
    }
    public static void main(String[] args) {
        // calling display no argument
        display();

        // calling display name
        display("Khushal");

        // calling display age
        display(22);
    }
}
