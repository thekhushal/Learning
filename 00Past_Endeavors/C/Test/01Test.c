// Question 1

// #include <stdio.h>

// int main(){
//     int a = 1, b = 2, c;

//     printf("Value of a is %d and b is %d\n", a, b);

//     c = b; // 2
//     b = a; // 1
//     a = c; // 2

//     printf("Value swap completed\n");
//     printf("Value of a is %d and b is %d\n", a, b);
//     return 0;
// }

// Question 2

// #include <stdio.h>
// int main(){
//     int a = 0, b = 1;

//     printf("Value of a is %d and b is %d\n", a, b);

//     a = a + b;
//     b = a - b;
//     a = a - b;

//     printf("Value swap completed\n");
//     printf("Value of a is %d and b is %d\n", a, b);
//     return 0;
// }

// Question 3

// #include <stdio.h>

// int main(){
//     char c;

//     printf("Enter a variable: \n");
//     scanf("%c",&c);

//     if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
//         printf("%c is a vowel", c);
//     } else{
//         printf("This is not a vowel");
//     }


//     return 0;
// }

// Question 4 

// #include <stdio.h>

// int main(){
//     int num;

//     printf("Enter the number: \n");
//     scanf("%d", &num);
    
//     if (num % 2 == 0){
//         printf("The number you've entered an even");
//     } else{
//         printf("The number you've entered is odd");
//     }

//     return 0;
// }

// Question 5

// #include <stdio.h>

// int main(){
//     int num;
    
//     printf("Enter a number: \n");
//     scanf("%d", &num);

//     if (num % 21 == 0){
//         printf("Input is valid");
//     } else {
//         printf("Input is not valid");
//     }
    
// }

// Question 6

// #include <stdio.h>
// int main(){
//     char c;

//     printf("Enter a variable: \n");
//     scanf("%c",&c);

//     if (c == 'q' || c == 'w' || c == 'e' || c == 'r' || c == 't' || c == 'y' || c == 'u' || c == 'i' || c == 'o' || c == 'p'){
//         printf("%c is in upper line", c);
//     } else{
//         printf("Invalid");
//     }


//     return 0;
// }

// Question 7

// #include <stdio.h>

// int main(){
//     int a, b;

//     printf("Enter first number: \n");
//     scanf("%d", &a);
//     b = a;

//     printf("Enter second number: \n");
//     scanf("%d", &a);
//     a = a + b;

//     printf("Value of a is updated to %d \n", a );
//     return 0;
// }

// Question 9

// #include <stdio.h>

// int main(){
//     int a = 0, b = 9, c = 2;

//     if (a > b && a > c)
//     {
//         printf("%d is the greatest of all", a);
//     } else if (b > a && b > c)
//     {
//         printf("%d is the greatest of all", b);
//     } else
//     {
//         printf("%d is the greatest of all", c);
//     }

// Question 8

// #include <stdio.h>
// int main(){
//     int inhand, salary, holiday;

//     printf("Enter your Salary and number of holidays you took: \n");
//     scanf("%d%d", &salary, &holiday);

//     if (holiday <= 1){
//         inhand = salary;
//     } 
//     else if (2 <= holiday && holiday < 5){
//         inhand = (salary/100)*5;
//         inhand = salary - inhand;
//     } 
//     else if (5 <= holiday && holiday <= 14){
//         inhand = (salary/100)*10;
//         inhand = salary - inhand;
//     } 
//     else if (holiday == 15){
//         inhand = (salary/100)*50;
//         inhand = salary - inhand;
//     } 
//     else {
//         inhand = 0;
//     }

//     printf("Final Salary comes out to be %d", inhand);

//     return 0;
// }

// Question 10

// #include <stdio.h>
// int main(){
//     int Grosssalary, BasicSalary, HRA, DA;

//     printf("Enter your salary here: \n");
//     scanf("%d", &BasicSalary);

//     if (BasicSalary >0 && BasicSalary <= 10000) {
//         HRA = (BasicSalary/100)*20;
//         DA = (BasicSalary/100)*80;
//         Grosssalary = BasicSalary + HRA + DA;
//     }
//     else if (BasicSalary > 10000 && BasicSalary <= 20000) {
//         HRA = (BasicSalary/100)*25;
//         DA = (BasicSalary/100)*90;
//         Grosssalary = BasicSalary + HRA + DA;
//     }
//     else if (BasicSalary > 20000){
//         HRA = (BasicSalary/100)*30;
//         DA = (BasicSalary/100)*95;
//         Grosssalary = BasicSalary + HRA + DA;
//     }
//     else{
//         printf("invalid input");
//     }
//     printf("%d", Grosssalary);
//     return 0;
// }