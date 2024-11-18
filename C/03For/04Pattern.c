/*
1.1
*
**
***
****
*/

// #include <stdio.h>

// int main(){
//     int num;

//     printf("Enter a width of pattern: ");
//     scanf("%d", &num);

//     for (int LineNum = 1; LineNum <= num; LineNum++)
//     {
//         for (int StarNum = 1; StarNum <= LineNum; StarNum++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }

/*
1.2
****
***
**
*
*/
// #include <stdio.h>

// int main(){
//     int num;

//     printf("Enter a width of pattern: ");
//     scanf("%d", &num);

//     for (int LineNum = num; LineNum >= 1; LineNum --){
//         for (int StarNum = 1; LineNum - StarNum >= 0; StarNum++){
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }

/*
1.3
*
**
***
****
***
**
*
*/

// #include <stdio.h>

// int main(){
//     int num, line;

//     printf("Enter a width of pattern: ");
//     scanf("%d", &num);

//     line = (num*2)-1;
//     for(int LineNum = 1;  LineNum <= line; LineNum++)
//     {
//         for(int Star = 1; Star <= LineNum && LineNum <= num; Star++)
//         {
//             printf("*");
//         }
//         for(int Star = 1; LineNum > num && Star <= (line - LineNum + 1); Star++) 
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
// }


/*
1.4
****
***
**
*
**
***
****
*/

// #include <stdio.h>

// int main(){
//     int num;

//     printf("Enter a width of Pattern: ");
//     scanf("%d", &num);

//     for(int Line = 1; Line <= num; Line++){
//         for(int Star = 0; Star <= num - Line; Star++){
//             printf("*");
//         }
//         printf("\n");
//     }

//     for (int Line = 1; Line <= num-1; Line++){
//         for(int Star = 0; Star <= Line; Star++){
//             printf("*");
//         }
//         printf("\n");
//     }

// }