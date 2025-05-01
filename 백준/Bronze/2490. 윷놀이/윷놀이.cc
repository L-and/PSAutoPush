#include <iostream>
using namespace std;

int main()
{
    int y[4];

    for(int _=0; _<3;_++)
    {
    cin>>y[0]>>y[1]>>y[2]>>y[3];

    int cnt = 0;

    for(int i=0;i<4;i++)
    {
        if(y[i] == 0) cnt++;
    }

    char result;
    switch(cnt)
    {
        case 0:
            result = 'E';
            break;
        case 1:
            result = 'A';
            break;
        case 2:
            result = 'B';
            break;
        case 3:
            result = 'C';
            break;
        case 4:
            result = 'D';
            break;
    }
    cout<<result<<endl;
    }
    return 0;
}