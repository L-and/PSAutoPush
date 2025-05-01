#include <iostream>
#include <vector>

using namespace std;

void printFiboCnt(int n, vector<pair<int, int>>& cntList)
{
    if(cntList.size() <= n)
    {
        for(int i=cntList.size(); i<=n; i++)
        {
            pair<int, int> newCnt = make_pair(cntList[i-2].first + cntList[i-1].first, cntList[i-2].second + cntList[i-1].second);
            cntList.push_back(newCnt);
        }
    }

    cout<<cntList[n].first<<' '<<cntList[n].second<<endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin>>t;

    vector<pair<int, int>> cntList;
    cntList.push_back(make_pair(1, 0));
    cntList.push_back(make_pair(0, 1));


    for(int i=0; i<t; i++)
    {
        int n;

        cin>>n;
        printFiboCnt(n,cntList);
    }
}