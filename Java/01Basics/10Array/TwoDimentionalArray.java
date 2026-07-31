import java.util.Arrays;

public class TwoDimentionalArray {
    public static void main(String[] args) {
        // Creating 2 D array (empty)
        int[][] mat = new int[3][4];

        // Creating 2D Array (and initializing using shortcut)
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Acessing Matrix
        System.out.println(mat[0][2]);
        System.out.println(matrix[2][1]);

        // Updating Element
        matrix[1][2] = 100;

        // Array Length
        System.out.println(matrix.length); // matrix.length gives number of rows
        System.out.println(matrix[2].length); // matrix[i].length gives number of column in i'th row

        // Jaged Array
        int[][] arr = {
            {1, 2},
            {3, 4, 5},
            {6}
        };
        
        // Array Length: Jaged Array
        System.out.println(arr.length); // arr.length still gives number of rows
        System.out.println(arr[0].length); // length of 0'th row; and if it were in a loop, length i'th row would give different result each time
    }
}
