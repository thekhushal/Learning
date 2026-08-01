public class StringBuilderMethods {
    public static void main(String[] args) {

        // ==========================================================
        // Creating StringBuilder
        // ==========================================================
        // StringBuilder sb1 = new StringBuilder();            // Empty
        StringBuilder sb2 = new StringBuilder("Java");      // With initial text

        System.out.println("Original: " + sb2);

        // ==========================================================
        // append()
        // Adds text at the end
        // ==========================================================
        sb2.append(" Programming");
        System.out.println("append(): " + sb2);

        // ==========================================================
        // insert(index, value)
        // Inserts text at a specified index
        // Valid index: 0 to length()
        // ==========================================================
        sb2.insert(4, " &");
        System.out.println("insert(): " + sb2);

        // ==========================================================
        // delete(start, end)
        // Removes characters from start to end-1
        // ==========================================================
        sb2.delete(4, 6);
        System.out.println("delete(): " + sb2);

        // ==========================================================
        // replace(start, end, str)
        // Replaces characters from start to end-1
        // ==========================================================
        sb2.replace(5, 16, "Builder");
        System.out.println("replace(): " + sb2);

        // ==========================================================
        // reverse()
        // Reverses the characters
        // ==========================================================
        sb2.reverse();
        System.out.println("reverse(): " + sb2);

        // Reverse again to restore
        sb2.reverse();

        // ==========================================================
        // length()
        // Returns number of characters
        // ==========================================================
        System.out.println("length(): " + sb2.length());

        // ==========================================================
        // charAt(index)
        // Returns character at given index
        // ==========================================================
        System.out.println("charAt(0): " + sb2.charAt(0));

        // ==========================================================
        // setCharAt(index, ch)
        // Replaces character at given index
        // ==========================================================
        sb2.setCharAt(0, 'j');
        System.out.println("setCharAt(): " + sb2);

        // ==========================================================
        // toString()
        // Converts StringBuilder to String
        // ==========================================================
        String str = sb2.toString();
        System.out.println("toString(): " + str);



        // ==========================================================
        // Edge Cases
        // ==========================================================

        // append() accepts different data types
        StringBuilder edge = new StringBuilder();
        edge.append(100);
        edge.append('A');
        edge.append(true);
        edge.append(3.14);
        System.out.println("\nappend() multiple types: " + edge);

        // insert() at beginning and end
        StringBuilder temp = new StringBuilder("Java");
        temp.insert(0, "I Love ");
        temp.insert(temp.length(), "!");
        System.out.println("insert() edges: " + temp);

        // delete entire content
        temp.delete(0, temp.length());
        System.out.println("delete all: \"" + temp + "\"");

        // replace() with longer and shorter strings
        StringBuilder rep = new StringBuilder("abcdef");
        rep.replace(2, 4, "XYZ");
        System.out.println("replace longer: " + rep);

        rep.replace(2, 5, "Q");
        System.out.println("replace shorter: " + rep);

        // reverse empty builder
        StringBuilder empty = new StringBuilder();
        empty.reverse();
        System.out.println("reverse empty: \"" + empty + "\"");



        // ==========================================================
        // Common Exceptions
        // Uncomment one at a time to test.
        // ==========================================================

        // StringBuilder ex = new StringBuilder("Java");

        // ex.charAt(10);            // StringIndexOutOfBoundsException
        // ex.setCharAt(10, 'X');    // StringIndexOutOfBoundsException
        // ex.insert(100, "Hi");     // StringIndexOutOfBoundsException
        // ex.delete(2, 20);         // StringIndexOutOfBoundsException
        // ex.replace(5, 10, "X");   // StringIndexOutOfBoundsException



        // ==========================================================
        // Quick Notes
        // ==========================================================
        /*
         * append()      -> Adds at end
         * insert()      -> Inserts at index
         * delete()      -> Removes [start, end)
         * replace()     -> Replaces [start, end)
         * reverse()     -> Reverses characters
         * length()      -> Number of characters
         * charAt()      -> Character at index
         * setCharAt()   -> Modify one character
         * toString()    -> Convert to String
         *
         * StringBuilder is MUTABLE.
         * Most methods modify the SAME object.
         * No need to assign the result back like String.
         *
         * String:
         *   s = s.toUpperCase();
         *
         * StringBuilder:
         *   sb.append("Java");   // Original object changes
         */
    }
}