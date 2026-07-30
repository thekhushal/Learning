public class While {
    public static void main(String[] args) {
        int i = 1;
        while(i <= 20){
            if (i%3 == 0){
                i++;
                continue;
            }
            System.out.print(i++ + "    ");
        }
        System.out.println();
    }
}
// while: 
// Write a program that prints numbers from 1 to 20, except multiples of 3.