#include <stdio.h>
int main()
{
    char op;
    int n1, n2;
    printf("Enter Operator(+, -, *, /, %%): ");
    op = getchar();
    printf("Enter two no.'s: ");
    scanf("%d %d", &n1, &n2);
    switch (op)
    {
        case '+' :
            printf("sum = %d \n", n1 + n2);
            break;
        case '-' :
            printf("Difference = %d \n", n1 - n2);
            break;
        case '*' :
            printf("Product = %d \n", n1*n2);
            break;
        case '/' :
            printf("Quotient = %d \n", n1 / n2);
            break;
        case '%' :
            printf("Remainder = %d \n", n1 % n2);
            break;
        default:
            printf("Unknown operation, Please try again");
    } // end of switch
    return 0;
} // end of main