/*
111111
2   2 
3  3  
4 4   
55    
6     
55    
4 4   
3  3  
2   2 
111111
*/

#include <stdio.h>

int main(){
    setbuf(stdout, NULL);
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    for (int line = 1; line <= num; line++){
        for (int j = 1; j <= num; j++){
            if (line == 1 || j == 1 || j == (num - line) + 1){
                printf("%d", line);
            }
            else{
                printf("|");
            }
        }
        printf("\n");
    }

    for (int line = num - 1; line > 0; line --){
        for (int j = 1; j <= num; j++){
            if (line == 1 || j == 1 || j == (num - line) + 1){
                printf("%d", line);
            }
            else{
                printf("|");
            }
        }
        printf("\n");
    }
}