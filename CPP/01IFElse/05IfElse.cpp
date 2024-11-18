#include <iostream>
using namespace std;

int main(){
    char ch;

    if (isalpha(ch))
    {
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
        ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
        {
            cout << ch << " Is a vouvel" << endl;
        } else {
        cout << ch << " is a consonant." << endl;
        }
    } else if (isdigit(ch)) {
        cout << ch << " Is a digit" << endl;
    } else {
        cout << ch << " Is a special character" << endl;
    }
}
