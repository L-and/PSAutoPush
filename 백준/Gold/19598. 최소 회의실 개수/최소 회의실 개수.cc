#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>

using namespace std;

bool compare(const pair<int, int>& p1, const pair<int, int>& p2)
{
    return p1.first < p2.first;
}

void solution1(std::vector<std::pair<int, int>> &timeList, int n, int &result)
{
    // 회의 시작시간으로 오름차순정렬
    sort(timeList.begin(), timeList.end(), compare);

    // 회의실마다의 종료시간을 저장할 변수
    vector<int> meetingEndTime(n, -1);

    for (auto time : timeList)
    {

        for (auto endTime = meetingEndTime.begin(); endTime != meetingEndTime.end(); endTime++)
        {
            if (*endTime <= time.first)
            {
                if (*endTime == -1)
                    result++;

                *endTime = time.second;
                break;
            }
        }
    }
}

void solution2(std::vector<std::pair<int, int>> &timeList, int n, int &result)
{
    // 회의 시작시간으로 오름차순정렬
    sort(timeList.begin(), timeList.end(), compare);

    // 시작시간으로 정렬 timeList에서 1~n번째 회의까지 반복하며
    // 회의 종료시간을 기준으로 회의진행 큐(우선순위 큐)를 만들고, 
    //제일 빨리끝나는 회의(큐의 루트노드)가 i번 회의의 시작시간과 같거나 크다면 POP 후 i번회의의 종료시간을 PUSH해줌
    // 최종 큐의 크기가 결과값

    // 시간복잡도
    // for loop : n, POP: log N, PUSH: log N
    // 총 O(N * log N) 예상

    // 최소힙으로 우선순위큐 생성
    priority_queue<int, vector<int>, greater<int>> meetingRoom;

    for (auto time : timeList)
    {
        if(meetingRoom.empty())
        {
            result++; // 회의실을 새로잡았으니 갱신
            meetingRoom.push(time.second);
        }

        else
        {
            int currentEndTime = meetingRoom.top(); // 현재 진행중인 회의중 가장빨리끝나는 시간

            // 내 회의가 현재 진행중인 회의실에서 가능하다
            if(currentEndTime <= time.first)
            {
                meetingRoom.pop(); // 현재 진행중인 회의를 끝내고
                meetingRoom.push(time.second); // 내 회의의 종료시간을 넣어줌
            }
            else // 새 회의실을 잡는경우
            {
                result++; // 회의실을 새로잡았으니 갱신
                meetingRoom.push(time.second); // 내 회의의 종료시간을 넣어줌
            }
        }
    }
}


int main()
{
    int n;
    cin>>n;

    vector<pair<int, int>> timeList(n);

    for(int i=0;i<n;i++) cin>>timeList[i].first>>timeList[i].second;

    // 회의 시작시간으로 오름차순정렬
    sort(timeList.begin(), timeList.end(), compare);

    
    int result = 0;

    // solution1(timeList, n, result); // 냅다구현

    solution2(timeList, n, result); // 큐사용

    cout<<result;
}