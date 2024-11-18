#include <stdio.h> 

int main(){
    int num,rev = 0;

    printf("Enter a number: \n");
    scanf("%d", &num);

    while (num >= 1){
        rev = (rev*10) + (num % 10);
        num = num / 10;
    }
    if (num / rev == 1) 
    {printf("Number is a palindrome number");}
    else 
    {printf("Number is not palindrome");}

    
}