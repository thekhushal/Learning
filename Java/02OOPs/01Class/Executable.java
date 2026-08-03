class Executable {
    public static void main(String[] args) {
        Main myObj1 = new Main(); // object 1
        Main myObj2 = new Main(); // onject 2
 
        System.out.println("Calling the class Main and accessing it through an object: "+myObj1.x);
        System.out.println("Adding the two attributes of class Main: "+myObj2.y + myObj2.x);
        // Main myObj3 = new Main(myObj2);
    }
}
