#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, m;
    cin>>n>>m;

    vector<int> mins(n, 0);
    for(int i=0;i<n;i++) cin>>mins[i];

    long start=*max_element(mins.begin(), mins.end());
    long end=100000*10000;
    long mid;

    while(start<end)
    {
        mid = (start+end)/2;

        vector<int> blurays(1, 0);
        for(int i=0; i<n;i++)
        {
            if(blurays.back()+mins[i] <= mid) blurays.back()+=mins[i];
            else blurays.push_back(mins[i]);
        }

        if(blurays.size() <= m)
        {
            end=mid;
        }
        else
            start=mid+1;
    }
    
    cout<<end;

    return 0;
}