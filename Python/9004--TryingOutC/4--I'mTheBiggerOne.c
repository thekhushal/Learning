#include<stdio.h>
int main ()
{
    int a, b ,c;
    printf("Enter no.'s : ");
    scanf("%d %d %d", &a, &b, &c);
    if (a > b)
    {
        if (a > c)
        {
            printf("%d is the largest no. \n", a);
        }
        else 
        {
            printf("%d is the largest no. \n", c);
        }
    }

    else
    {
        if (b > c)
        {
            printf("%d is the largest no. \n", b);
        }
        else 
        {
            printf("%d is the largest no. \n", c);
        }
    }
}