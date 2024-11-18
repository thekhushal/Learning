#include <stdio.h>

int main(){
    int num1, num2, gcd = 1, divisor = 2;

    printf("Enter First numbers: ");
    scanf("%d", &num1);
    printf("Enter Second numbers: ");
    scanf("%d", &num2);

    while (num1 > 1 || num2 > 1)
    {
        if (num1 % divisor == 0 && num2 % divisor == 0)
        {
            gcd = gcd * divisor;
            num1 = num1 / divisor;
            num2 = num2 / divisor;
        } 
        else if (num1 % divisor == 0 && num2 % divisor != 0)
        {
            num1 = num1 / divisor;
        }
        else if (num1 % divisor != 0 && num2 % divisor == 0)
        {
            num2 = num2 / divisor;
        }
        else{
            divisor++;
        }
        
    }
    printf("Greateest common divisor is %d", gcd);
    
}