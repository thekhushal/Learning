/*
2.1
1111
222
33
4
*/
#include <stdio.h>

int main(){
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    for(int i = 1; i <= num; i++){
        for(int j = i; j <= num; j++){
            printf("%d", i);
        }
        printf("\n");
    }
}