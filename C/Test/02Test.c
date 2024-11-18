#include <stdio.h>
int main(){
    
    int a, b = 1, c;
    printf("Enter a number: ");
    scanf("%d", &a);

    for (c = 1; c <= a; c++) {
        b *= c;
    }

    printf("Factorial of %d is %d\n", a, b);
    return 0;

    
}


#include <stdio.h>

int power(int x, int y) {
    int result = 1;
    for (int i = 0; i < y; i++) {
        result *= x;
    }
    return result;
}

void checkNumber(int num) {
    int original, reversed = 0, r, n = 0, sum = 0, temp;

    original = num;
    while (original != 0) {
        r = original % 10;
        reversed = reversed * 10 + r;
        original /= 10;
    }

    if (reversed == num) {
        printf("%d is a Palindrome number.\n", num);
    } else {
        printf("%d is not a Palindrome number.\n", num);
    }

    original = num;
    temp = num;

    while (temp != 0) {
        temp /= 10;
        n++;
    }

    while (original != 0) {
        r = original % 10;
        sum += power(r, n);
        original /= 10;
    }

    if (sum == num) {
        printf("%d is an Armstrong number.\n", num);
    } else {
        printf("%d is not an Armstrong number.\n", num);
    }
}

int main() {
    int number;
    printf("Enter an integer: ");
    scanf("%d", &number);
    checkNumber(number);
    return 0;
}


















// #include <stdio.h>

// int main(){
//     char a, shape;

//     printf("Press a to cal Area, press v to cal Volume: ");
//     scanf("%c", &a);

//     if (a == 'a')
//     {
//         printf("To calculate area press  t - Triangle  s - Square  r - rectangle: ");
//         scanf("%c", &shape);

//         if (shape == 't')
//         {
//             int base, height, area;

//             printf("Height of Triangle: ");
//             scanf("%d", &height);
//             printf("Base of Triangle: ");
//             scanf("%d", &base);

//             area = (base * height) / 2;
//             printf("%d", area);
//         }
//         else if (shape == 's')
//         {
//             int length, breadth, area;

//             printf("Length: ");
//             scanf("%d", &length);
//             printf("Breadth: ");
//             scanf("%d", &breadth);

//             area = (length * breadth);
//             printf("%d", area);
//         }
//         else if (shape == 'r')
//         {
//             int length, breadth, area;

//             printf("Length: ");
//             scanf("%d", &length);
//             printf("Breadth: ");
//             scanf("%d", &breadth);

//             area = (length * breadth);
//             printf("%d", area);
//         }
//         else
//         {
//             printf("Input invalid");
//         }
//     }
//     else
//     {
//         printf("Volume of 2D Figure cannot be calculated");
//     }
// }