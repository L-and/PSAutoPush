// 목표
// -10억~ +10억의특성값을 가지는 용액중 2개의 용액을 섞어서
// 0과 가장 가까운 값을 만드는 2개의 용액을 찾는 것

// 범위
// n: 10만개 이하
// 용액 특성값: -10억~+10억
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    cin>>n;

    vector<int> v(n, 0);

    for(int i=0;i<n;i++) 
    {
        cin>>v[i];
    }
    
    sort(v.begin(), v.end());

    int r[2];

    int minPh = INT32_MAX;
    int start=0;
    int end=n-1;

    while(start<end)
    {   
        int sum = v[start]+v[end];

        if(abs(sum)<minPh)
        {
            minPh = abs(sum);
            r[0]=start,r[1]=end;
        }

        if(sum > 0)
        {
            end--;
        }
        else
        {
            start++;
        }

        
    }
    
    cout<<v[r[0]]<<' '<<v[r[1]];
    

    return 0;
}