#include <iostream>

using namespace std;

int main()
{
    long long target;
    cin>>target;

    long long current=0;
    long long cnt=0;

    while(target>current)
    {
        cnt++;

        if(current ==0) current++;
        else    current *=2;
    }

    cout<<cnt;
    
    return 0;
}