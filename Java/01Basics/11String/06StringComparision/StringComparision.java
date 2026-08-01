public class StringComparision {
    public static void main(String[] args) {
//      == compares references 
//          == asks:
//              "Do these two variables point to the same object?"
//               It does not ask whether the text is the same.

//      .equals() compares the contents
        String s1 = "Java";
        String s2 = "Java";

        System.out.println(s1.equals(s2)); // True


//      Java stores string literals in a special memory area called the String Pool.
//      Due to that s1 and s2 point to same object which is java
        System.out.println(s1 == s2); // True

//      But it won't work if both are new object, as they will point at different location in that case
        String s11 = new String("Java");
        String s12 = new String("Java");

        System.out.println(s11 == s12);
    }
}
