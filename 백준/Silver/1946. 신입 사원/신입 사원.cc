#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;



bool compare(const pair<int, int>& p1, const pair<int, int>& p2)
{
    return p1.first > p2.first;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin>>t;

    for(int _t=0; _t<t; _t++)
    {
        int n;
        cin>>n;
        
        vector<pair<int, int>> rankList(n, pair<int, int>());
        for(int i=0;i<n;i++) cin>>rankList[i].first>>rankList[i].second;

        // 서류심사 등수의 내림차순으로 정렬
        sort(rankList.begin(), rankList.end(), compare);

        int cnt = 0; // 통과한 사람의 수

        // 방법2
        vector<bool> doneRank(n,false); // 남아있는 인원들의 심사여부

        int passRank = 1; // 심사에 통과하는 등수

        for(int i=0; i<n; i++)
        {
            int& myRank = rankList[i].second; // i번째 사람의 면접등수

            if(passRank == myRank) // 통과
            {
                cnt++;
            }

            doneRank[myRank-1] = true; // 심사완료로 변경

            // 심사통과등수 업데이트
            while(doneRank[passRank-1] == true)
            {
                passRank++;
            }
        }
        
        
        cout<<cnt<<'\n';
    }

    return 0;
}