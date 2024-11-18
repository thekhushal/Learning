#include <stdio.h>

int main(){
    int num, divisor = 1, perfect = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

while(divisor <  num){
    if(num % divisor == 0) {
        perfect = perfect + divisor;
    }
    divisor ++;
}

if (num == perfect) 
    {printf("Number is a perfect number");}
    else{
    printf("Not a perfect number");
}
return 0;
} 