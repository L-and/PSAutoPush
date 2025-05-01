#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>

using namespace std;

class Beer
{
    public:
    int preference;
    int alcohol;

    Beer(){}

    bool operator<(const Beer& b) const {
        return this->preference > b.preference;
    }
};

bool compare(Beer& a, Beer& b)
{
    return (a.alcohol < b.alcohol);
}

int main()
{
    int n; // 축제기간
    int m; // 선호도의 합
    int k; // 맥주의 종류 갯수

    cin>>n>>m>>k;

    vector<Beer> beerList(k, Beer()); // 맥주의 선호도, 도수레벨

    for(int i=0;i<k;i++) cin>>beerList[i].preference>>beerList[i].alcohol;

    // 알코올기준 오름차순 정렬
    sort(beerList.begin(), beerList.end(), compare);


    // 먹어볼 맥주를 저장
    priority_queue<Beer> box;
    int boxPreference = 0;

    // 알코올이 적은순으로 정렬했으니, box에 넣으며 result를 갱신해가면 정답이 나옴
    int result = 0;

    // 맥주들을 알코올이 적은순으로 box에 추가
    for(int i=0;i<k;i++)
    {
        // n개의 맥주를 담았으면, 맥주들의 선호도 합이 m이상인지 확인
        if(box.size() == n)
        {
            // 선호도가 m이상이면 검사완료
            if(boxPreference >= m) break;
            else // 선호도가 부족하면, 선호도가 제일적은 맥주를 빼줌
            {
                // 현재선호도 재설정
                boxPreference -= box.top().preference;
                box.pop();
            }
        }

        
        // 현재선호도, 최소알코올값 재설정
        boxPreference += beerList[i].preference;
        result = beerList[i].alcohol;

        box.push(beerList[i]); // box에 맥주추가
    }

    // 모든 맥주를 검사했음에도 선호도를 만족하지못하면 result로 -1저장
    if(boxPreference < m)
    {
        result = -1;
    }

    cout<<result;

    return 0;
}