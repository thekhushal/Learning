#include <iostream>
using namespace std;

int main(){
    int year;
    cout << "Enter a number: "; cin >> year;

    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        cout << "It is leap year";
    } else {
        cout << "It isn't a leap year";
    }
}