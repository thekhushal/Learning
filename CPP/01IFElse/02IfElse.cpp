#include <iostream>
using namespace std;

int main() {
    int a;
    cout << "Press in a number" << endl ; cin >> a;

    if ( a < 0 ) {
        cout << "The number is negative" << endl;
    } else if ( a > 0 ) {
        cout << "The number is positive \n";
    } else {
        cout << "You pressed zero \n ";
    }
}