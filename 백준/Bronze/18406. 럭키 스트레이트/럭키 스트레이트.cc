#include <iostream>
using namespace std;

int main()
{
    string n;
    cin >> n;

    int left=0, right=0;
    for(int i=0; i<n.size()/2; i++) left += (n[i]-48);
    for(int i=n.size()/2; i<n.size(); i++) right += (n[i]-48);

    if (left == right) cout << "LUCKY";
    else cout << "READY";

    return 0;
}