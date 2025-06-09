#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    for(int i=0; i<n; i++)
    {
        string password;
        cin >> password;

        if (password.length() >= 6 && password.length() <= 9)
            cout << "yes\n";
        else
            cout << "no\n";
    }

    return 0;
}