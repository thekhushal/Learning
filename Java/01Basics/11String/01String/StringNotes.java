public class StringNotes {
    public static void main(String[] args){
        // Creating a String
        String city = "Jaipur"; // String stores a sequence of characters, its a class
        
        // Alternate way to create a string
        String state = new String("Rajasthan");

        // Printing String
        System.out.println(city);

        // String Length
        System.out.println(state.length()); //Notice: Array uses .length (no parenthesis), but string uses method .length()

        // Accessing Characters: .charAt() method
        System.out.println(city.charAt(3)); // it access character at 3'rd index 
        // System.out.println(city[4]); // ERROR: not the right way to acess string char

        // Accessing last character
        System.out.println(state.charAt(state.length() - 1));

        // Strings are Immutable
        String s = "Java";
        // s.charAt(0) = 'j'; // we can't do this 
        s = "java"; // But this is allowed
        System.out.println(s);
        
        // 
    }
}
