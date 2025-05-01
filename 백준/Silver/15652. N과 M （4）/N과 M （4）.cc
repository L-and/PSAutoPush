#include <iostream>
#include <vector>
using namespace std;

void solve(int n, int m, vector<int>& result, int last)
{
    if(result.size() == m)
    {
        for(auto v: result) cout<<v<<' ';
        cout<<'\n';
        return;
    }

    for(int i=last;i<=n;i++)
    {
        result.push_back(i);
        solve(n, m, result, i);
        result.pop_back();
    }
}

int main()
{
    int n,m;

    cin>>n>>m;

    vector<int> result;

    solve(n,m, result, 1);

    return 0;
}