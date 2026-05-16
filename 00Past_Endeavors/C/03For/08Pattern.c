/*
1 2 3 4 5 6 5 4 3 2 1 
1       5   5       1 
1     4       4     1 
1   3           3   1 
1 2               2 1 
1                   1 
1 2               2 1 
1   3           3   1 
1     4       4     1 
1       5   5       1 
1 2 3 4 5 6 5 4 3 2 1 
*/

#include <stdio.h>

int main(){
    int size;

    printf("How long do you want the pattern to be: ");
    scanf("%d", &size);

    size = (size + 1) / 2;

    for (int line = 1; line <= size; line ++)
    {
        for (int column = 1; column <= size; column ++){
            if (line == 1 || column == 1 || column == (size - line) + 1){
                printf("%d ", column);
            }else{
                printf("  ");
            }
        }
        for (int column = size - 1; column >= 1; column --){
            if (line == 1 || column == 1 || column == (size - line) + 1){
                printf("%d ", column);
            }else{
                printf("  ");
            }
        }
        printf("\n");
    }

    for (int line = size - 1; line >= 1; line -- )
    {
        for (int column = 1; column <= size; column ++){
            if (line == 1 || column == 1 || column == (size - line) + 1){
                printf("%d ", column);
            }else{
                printf("  ");
            }
        }
        for (int column = size - 1; column >= 1; column --){
            if (line == 1 || column == 1 || column == (size - line) + 1){
                printf("%d ", column);
            }else{
                printf("  ");
            }
        }
        printf("\n");
    }

    return 0;
}