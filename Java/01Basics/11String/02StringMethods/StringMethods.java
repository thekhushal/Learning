public class StringMethods {

    public static void main(String[] args) {

        // =====================================================
        // SAMPLE STRINGS
        // =====================================================
        String s1 = "Java";
        String s2 = "java";
        String text = "Programming";
        String spaced = "   Hello Java   ";

        // =====================================================
        // length()
        // Returns the number of characters.
        // =====================================================
        System.out.println(s1.length());            // 4
        System.out.println("".length());            // 0 (empty string)

        // =====================================================
        // charAt(index)
        // Returns the character at the given index.
        // Valid index: 0 to length()-1
        // =====================================================
        System.out.println(s1.charAt(0));           // J
        System.out.println(s1.charAt(3));           // a

        // Runtime Exception:
        // s1.charAt(4);      // StringIndexOutOfBoundsException
        // s1.charAt(-1);     // StringIndexOutOfBoundsException

        // =====================================================
        // equals()
        // Case-sensitive comparison.
        // =====================================================
        System.out.println(s1.equals(s2));          // false
        System.out.println(s1.equals("Java"));      // true
        System.out.println(s1.equals(null));        // false (safe)

        // DON'T DO THIS:
        // String x = null;
        // x.equals("Java");      // NullPointerException

        // Safe way:
        System.out.println("Java".equals(s1));

        // =====================================================
        // equalsIgnoreCase()
        // Ignores letter case.
        // =====================================================
        System.out.println(s1.equalsIgnoreCase(s2));   // true

        // =====================================================
        // toUpperCase()
        // Does NOT modify original string.
        // =====================================================
        System.out.println(s1.toUpperCase());       // JAVA
        System.out.println(s1);                     // Java

        s1 = s1.toUpperCase();
        System.out.println(s1);                     // JAVA

        // =====================================================
        // toLowerCase()
        // =====================================================
        System.out.println(s1.toLowerCase());       // java

        // =====================================================
        // contains()
        // Case-sensitive.
        // =====================================================
        System.out.println(text.contains("gram"));  // true
        System.out.println(text.contains("Gram"));  // false
        System.out.println(text.contains("Java"));  // false

        // =====================================================
        // indexOf()
        // Returns first occurrence.
        // Returns -1 if not found.
        // =====================================================
        System.out.println(text.indexOf("g"));      // 3
        System.out.println(text.indexOf("m"));      // 6
        System.out.println(text.indexOf("z"));      // -1

        // =====================================================
        // substring(beginIndex)
        // Includes beginIndex.
        // Goes till end.
        // =====================================================
        System.out.println(text.substring(3));      // gramming

        // =====================================================
        // substring(beginIndex, endIndex)
        // beginIndex INCLUDED
        // endIndex EXCLUDED
        // =====================================================
        System.out.println(text.substring(3, 7));   // gram
        System.out.println(text.substring(0, 4));   // Prog

        // Runtime Exceptions:
        // text.substring(-1);
        // text.substring(20);
        // text.substring(5, 2);
        // text.substring(0, 20);

        // =====================================================
        // trim()
        // Removes leading and trailing whitespace only.
        // =====================================================
        System.out.println(spaced.trim());          // "Hello Java"
        System.out.println(spaced);                 // Original unchanged

        System.out.println(" A B ".trim());         // "A B"
        // Middle spaces remain.

        // =====================================================
        // Strings are Immutable
        // Every modifying method returns a NEW String.
        // =====================================================
        String str = "java";

        str.toUpperCase();
        System.out.println(str);                    // java

        str = str.toUpperCase();
        System.out.println(str);                    // JAVA

        // =====================================================
        // QUICK REMINDERS
        // =====================================================

        // Arrays:
        // arr.length

        // Strings:
        // str.length()

        // Last character:
        // str.charAt(str.length() - 1)

        // Last valid index:
        // str.length() - 1

        // Index not found:
        // indexOf(...) returns -1

        // substring(start, end):
        // start -> INCLUDED
        // end   -> EXCLUDED
    }
}
