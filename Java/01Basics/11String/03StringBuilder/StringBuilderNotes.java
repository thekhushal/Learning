public class StringBuilderNotes{
    public static void main(String[] args) {
        // StringBuilder 
        StringBuilder sb = new StringBuilder();

        // with an initial value
        StringBuilder ab = new StringBuilder("Java");

        // Why use string builder 
            // because strings are immutable, adding to a string (S = s+ "java") then again(s = s+ "learning") every time we do this we are creating a new string in the memory, its okay limited number of times, but when you are making a pdf or a text file of 1000's of words it becomes highly inefficient, java provides string builder to solve this very problem

        sb
    }
}