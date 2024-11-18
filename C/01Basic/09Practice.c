#include <stdio.h>

int main(){
    int number, prime = 3, divisor, isPrime;

    printf("Enter the number: ");
    scanf("%d", &number);

    printf("Following are the Prime number till %d\n", number);

    printf("- 2\n");

    while(prime < number){
        isPrime = 0;
        divisor = 3;
        while(divisor < prime){
            if(prime % divisor == 0){
                isPrime = 1;
                break;
            }
            divisor += 2;
        }
        if (isPrime == 0){
            printf("- %d\n", prime);
        }
        prime += 2;
    }
}