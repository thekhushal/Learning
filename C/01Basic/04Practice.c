#include <stdio.h>

int main(){
    int num;

    printf("Enter a number: \n");
    scanf("%d", &num);

    while(num > 1){
        printf("%d", num%10);
        num = num / 10;
    }
}