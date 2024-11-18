#include <stdio.h>

int main(){
    int num1, num2, divisor = 2;

    printf("Enter First numbers: ");
    scanf("%d %d", &num1, &num2);

    printf("Following are the Prime Factors of %d and %d: \n", num1, num2);
    while (num1 > 1 || num2 > 1)
    {
        if (num1 % divisor == 0 && num2 % divisor == 0)
        {
            printf("- %d \n", divisor);
            num1 = num1 / divisor;
            num2 = num2 / divisor;
        } 
        else if (num1 % divisor == 0 && num2 % divisor != 0)
        {
            printf("- %d \n", divisor);
            num1 = num1 / divisor;
        }
        else if (num1 % divisor != 0 && num2 % divisor == 0)
        {
            printf("- %d \n", divisor);
            num2 = num2 / divisor;
        }
        else{
            divisor++;
        }
        
    }
    
}