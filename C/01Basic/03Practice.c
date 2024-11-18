#include <stdio.h>

int main() {
    int num,sum = 0;
    char choice = 'c';

    while (choice == 'c'){
        printf("Enter a Number: \n");
        scanf("%d", &num);
        sum = sum + num;

        printf("To calculate sum Press 's' to continue press 'c': \n");
        scanf(" %c", &choice);
    }

    printf("The sum is: %d\n", sum);
}