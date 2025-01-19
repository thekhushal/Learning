#include <stdio.h>
int main()
{
    int n1, n2;
    printf("Enter two numbers: ");
    scanf("%d %d", &n1, &n2);
    printf("Sum = %d \n", n1+n2);
    printf("Difference = %d \n", n1-n2);
    printf("product = %d \n", n1*n2);
    printf("Quotient = %d \n", n1/n2);
    printf("Remainder = %d \n", n1%n2);
    return 0;
}
