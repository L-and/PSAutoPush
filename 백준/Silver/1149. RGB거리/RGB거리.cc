#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<vector<int>> costList(n);

    // Index:0 입력
    int r,g,b;
    cin >> r >> g>> b;
    costList[0].push_back(r);
    costList[0].push_back(g);
    costList[0].push_back(b);

    // 1~n 동안 (i-1)의 집 Cost에서 규칙에 해당하는(i와 다른 색깔의 집중 min값을 add)
    for(int i=1; i<n; i++)
    {
        vector<int>& prev = costList[i-1];
        vector<int>& cur = costList[i];
        cin >> r >> g >> b;
        cur.push_back(r);
        cur.push_back(g);
        cur.push_back(b);

        cur[0] += min(prev[1], prev[2]);
        cur[1] += min(prev[0], prev[2]);
        cur[2] += min(prev[0], prev[1]);

        // cout << prev[0] << ' '<<prev[1] << " "<<prev[2] << endl;
    }
    // cout << costList[n-1][0] << ' '<<costList[n-1][1] << " "<<costList[n-1][2] << endl;

    // get result
    int result = 5000000; 
    for(int i=0;i<3;i++)
    {
        result = (result > costList[n-1][i]) ? costList[n-1][i] : result;
    }

    cout << result;


    return 0;
}