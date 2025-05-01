#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin>>n;

    vector<int> req_budgets(n, 0);
    for(int i=0; i<n; i++) cin>>req_budgets[i];

    int total_budget;
    cin>>total_budget;

    int start=1;
    int end=*max_element(req_budgets.begin(), req_budgets.end());

    int mid;

    while(start<=end)
    {
        mid = (start+end)/2;
        // cout<<start<<' '<<mid<<' '<<end<<endl;

        int temp_budget = total_budget;
        for(int budget : req_budgets)
        {
            temp_budget -= min(mid, budget);
        }
        // cout<<temp_budget<<endl;
        if(temp_budget >= 0)
        {
            start = mid+1;
        }
        else
        {
            end = mid-1;
        }
    }

    cout<<end;
}