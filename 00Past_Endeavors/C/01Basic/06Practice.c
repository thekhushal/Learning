#include <stdio.h>
int main(){
    int num, num_, arm = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    num_ = num;

    while(num >= 1){
        arm += ((num % 10) * (num % 10) * (num % 10));
        num = num / 10;
    }

    if (num_ == arm)
    {printf("%d is an armstrong number", num_);}
    else
    {printf("%d is not an armstrong number", num_);}

}

/*
take input num
num % 10 * 3
num / 10 

*/