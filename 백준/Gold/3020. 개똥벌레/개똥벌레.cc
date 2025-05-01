#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    int n, h;
    cin >> n >> h;
    vector<int> topHeights;
    vector<int> bottomHeights;

    for(int i=0; i<n; i++) 
    {
        int tmp;
        cin >> tmp;
        if (i % 2 != 0) 
        {
            topHeights.push_back(tmp);
        }
        else
        {
            bottomHeights.push_back(tmp);
        } 
    }

    // 이분탐색을 위해 정렬
    sort(topHeights.begin(), topHeights.end());
    sort(bottomHeights.begin(), bottomHeights.end());

    vector<int> wallCountByHeight(h+1, 0);

    // cout << "TopHeights : ";
    // for (int h : topHeights) cout << h << ' ';
    // cout<<endl;

    // cout << "BottomHeights : ";
    // for (int h : bottomHeights) cout << h << ' ';
    // cout<<endl;

    for (int currentHeight=1;currentHeight<=h;currentHeight++)
    {
        int topWallBreakCount = upper_bound(topHeights.begin(), topHeights.end(), h - currentHeight) - topHeights.begin();
        wallCountByHeight[currentHeight] += topHeights.size() - topWallBreakCount;

        // cout << "검사중인 벽의 높이: " << h - currentHeight << "부숴지는 벽 갯수: " << wallCountByHeight[currentHeight]<<endl;
        
        int bottomWallBreakCount = lower_bound(bottomHeights.begin(), bottomHeights.end(), currentHeight) - bottomHeights.begin();
        wallCountByHeight[currentHeight] += bottomHeights.size() - bottomWallBreakCount;

        // cout << "검사중인 벽의 높이: " << currentHeight << "부숴지는 벽 갯수: " <<wallCountByHeight[currentHeight]<<endl;
    }

    // for(int i=1; i<=h; i++)
    // {
    //     cout << wallCountByHeight[i] << ' ';
    // }
    // cout<<endl;

    int minValue = *min_element(wallCountByHeight.begin() + 1, wallCountByHeight.end());
    int minCount = count(wallCountByHeight.begin() + 1, wallCountByHeight.end(), minValue);

    cout << minValue << ' ' << minCount;

    return 0;
}