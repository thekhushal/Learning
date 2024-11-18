/*
12345654321
1   5 5   1
1  4   4  1
1 3     3 1
12       21
1         1
*/


#include <stdio.h>

int main(){
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    for(int i = 0; i < num; i++) // num = 5 i = 4
    {
        for (int j = 1; j <= num; j++) //1;
        {
            if(i == 0 || j == 1 || j == num - i) // num - i = 1
            {
                printf("%d", j);
            }
            else
            {
                printf(" ");
            }
        }

        for (int j = num - 1; j > 0; j --)
        {
            if(i == 0 || j == 1 || j == num - i)
            {
                printf("%d",j);
            }
            else
            {
                printf(" ");
            }
        }
        
        printf("\n");
    }
}