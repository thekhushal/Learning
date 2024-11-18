#include <stdio.h>
int main(){
    int num, Digit, out;

    printf("Enter Number: ");
    scanf("%d", &num);

    while (num > 0){
        Digit = num % 10;
        out = (out * 10) + Digit;
        num = num /10;
        // PlaceHolder = PlaceHolder * 10;
    }
    
    printf("%d", out);
}