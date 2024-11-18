#include <iostream>
using namespace std;

int main(){
    int a;
    cout << "Enter your Percentage: ";
    cin >> a;

    if ( a > 100 ) {
        cout << "Kindly present a valid value \n";
    } else if (a == 100){
        cout << "Garibo pr thodi daya barsaiya \n";
    } else if (90 <= a && a < 100) {
        cout << "Itte mai tho 3 paas hjae \n";
    } else if (60 <= a && a < 90) {
        cout << "Aise kro ge maa baap ka naam roshan \n";
    } else if (33 <= a && a < 60) {
        cout << "Dhyan se beta \n";
    } else {
        cout << "Ab tho sambhal ja beta \n";
    }
    
}