public class Array {
    public static void main(String[] args){

        // First way to create array
        int[] numbers = new int[5];

        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;

        display_array(numbers);

        // Second method of creating array
        int[] arr = new int[5];

        for(int i = 0; i < 5; i++){
            arr[i] = 10*(i+1);
        }

        display_array(arr);

        // Third way to create array
        int[] five = {1,2,3,4,5};
        display_array(five);

    }

    static void display_array(int[] arr){
        for(int a = 0; a < arr.length; a++  ){
            System.out.println(arr[a]);
        }
        
        System.out.println("---------------------");
    }

}
