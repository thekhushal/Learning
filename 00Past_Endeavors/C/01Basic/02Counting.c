#include <stdio.h>

int main(){

    int num, ans, count = 1;

    printf("Enter a number: ");
    scanf("%d", &num);

    while(count <= 10){
        ans = num * count;
        printf("%d * %d = %d \n", num, count, ans);
        count++;
    }

    return 0;
}