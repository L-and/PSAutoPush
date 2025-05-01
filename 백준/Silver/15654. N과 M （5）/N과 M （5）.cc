#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve(int n, int m, vector<int>& result, vector<int>& nums)
{
    if(result.size() == m)
    {
        for(auto v: result) cout<<v<<' ';
        cout<<'\n';
        return;
    }

    for(int i=0;i<nums.size();i++)
    {
        bool isOk = true;
        for(auto v: result)
        {
            if(nums[i] == v) isOk = false;
        }
        
        if(isOk)
        {
        result.push_back(nums[i]);
        solve(n, m, result, nums);
        result.pop_back();
        }
    }
}

int main()
{
    int n,m;

    cin>>n>>m;

    vector<int> nums(n);

    for(int i=0;i<n;i++) cin>>nums[i];
    sort(nums.begin(), nums.end());

    vector<int> result;

    solve(n,m, result, nums);

    return 0;
}