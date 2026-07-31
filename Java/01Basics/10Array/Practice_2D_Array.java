public class Practice_2D_Array {
    public static void main(String[] args){
        int[][] mat ={
            {10, 20, 30}, 
            {40, 50, 60},
            {70, 80, 90}
        };
        print_matrix(mat);
    }

    static void print_matrix(int[][] arr){
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr[i].length; j++){
                System.out.print(arr[i][j] + "    ");
            }
            System.out.println();
        }

    }
}
/*
Create the following matrix:

10 20 30
40 50 60
70 80 90

Then:

Print the entire matrix using nested for loops.
Print only the second row.
Print only the third column.
*/