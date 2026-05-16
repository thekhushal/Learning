#include <stdio.h>

int main(){
    int num, divisor = 2;

    printf("Enter a number: ");
    scanf("%d", &num);

    printf("Following are the Prime Factors of %d: \n", num);
    while (num > 1)
    {
        if (num % divisor == 0)
        {
            printf("- %d \n", divisor);
            num = num / divisor;
        } 
        else{
            divisor++;
        }
        
    }
    
}