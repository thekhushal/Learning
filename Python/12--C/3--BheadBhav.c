#include<stdio.h>
int main ()
{
    int n;
    printf("Enter a no. : ");
    scanf("%d", &n);

    if (n % 2 == 0)
    {
        printf("The given no. is Even");
    }

    else
    {
        printf("The given no. is odd");
    }
    return 0;
}