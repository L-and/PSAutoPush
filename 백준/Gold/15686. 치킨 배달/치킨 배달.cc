#include <iostream>
#include <vector>
#include <utility>
#include <climits>

using namespace std;

void printPos(vector<pair<int, int>>& v)
{
    for(auto it=v.begin(); it!= v.end(); it++)
    {
        cout<<it->first<<','<<it->second<<' ';
    }
    cout<<endl;
}

class Combination
{
    vector<vector<pair<int, int>>> result;

    void combination(vector<pair<int ,int>>& posList, vector<pair<int, int>>& currentList, int start, int m)
    {
        if(currentList.size() == m)
        {
            result.push_back(currentList);
            return;
        }

        for(int i=start; i<posList.size(); i++)
        {
            currentList.push_back(posList[i]);
            combination(posList, currentList, i+1, m);
            currentList.pop_back();
        }
    }

    public:
    vector<vector<pair<int ,int>>> getCombination(vector<pair<int, int>>& posList, int m)
    {
        result.clear();
        vector<pair<int, int>> current;
        combination(posList, current, 0, m);

        return result;
    }
};

int main()
{
    int n,m;
    cin>>n>>m;
    
    vector<pair<int ,int>> chickenPosList;
    vector<pair<int ,int>> housePosList;

    for(int y=0;y<n;y++)
    {
        for(int x=0;x<n;x++)
        {
            int tmp;
            cin>>tmp;

            switch(tmp)
            {
                case 1:
                    housePosList.push_back(make_pair(x, y));
                    break;
                case 2:
                    chickenPosList.push_back(make_pair(x, y));
                    break;
            }
        }
    }

    // 이줄 이전까지 입력부분

    // printPos(chickenPosList);
    // printPos(housePosList);

    // chickenPos중 m개를 선택한 조합을 만들어서 
    // 가장 가까운 치킨집들의 최솟값을 계산
    
    Combination c;
    vector<vector<pair<int ,int>>> chickenPosCombination = c.getCombination(chickenPosList, m);

    int result = INT_MAX;

    // m개의 치킨집의 좌표리스트 반복
    for(auto combination: chickenPosCombination)
    {
        int cityDist=0;
        // 각 집의 치킨거리(가장 가까운 치킨집과의 거리)를 계산
        for(int i=0; i<housePosList.size(); i++)
        {
            int minDist=INT_MAX;
            for(auto chickenPos: combination)
            {
                // 집과 치킨집의 치킨거리를 구함(최소거리)
                    int chickenDistance = abs(chickenPos.first - housePosList[i].first) + abs(chickenPos.second - housePosList[i].second);
                    minDist = (minDist > chickenDistance) ? chickenDistance : minDist;
            }
            cityDist += minDist;
        }
        result = (result > cityDist) ? cityDist : result;

        
    }

    cout<<result;

    return 0;

}

