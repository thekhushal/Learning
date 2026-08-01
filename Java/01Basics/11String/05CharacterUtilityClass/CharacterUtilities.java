public class CharacterUtilities {
    public static void main(String[] args) {
        // 1. isLetter()
        System.out.println(Character.isLetter('A'));
        System.out.println(Character.isLetter('z'));
        System.out.println(Character.isLetter('5'));
        System.out.println(Character.isLetter('@'));

        // 2. isDigit()
        System.out.println(Character.isDigit('7'));
        System.out.println(Character.isDigit('A'));

        // 3. isUpperCase()
        System.out.println(Character.isUpperCase('A'));
        System.out.println(Character.isUpperCase('a'));

        // 4. isLowerCase()
        System.out.println(Character.isLowerCase('a'));
        System.out.println(Character.isLowerCase('A'));

        // 5. isWhitespace()
        System.out.println(Character.isWhitespace(' '));
        System.out.println(Character.isWhitespace('\n'));
        System.out.println(Character.isWhitespace('A'));

        // 6. toUpperCase()
        System.out.println(Character.toUpperCase('a'));
        System.out.println(Character.toUpperCase('z'));

        // 7. toLowerCase()
        System.out.println(Character.toLowerCase('A'));
        System.out.println(Character.toLowerCase('Z'));
    }
}
