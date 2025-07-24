#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iostream>
using namespace std;

bool compare(pair<long long, long long>& a, pair<long long, long long>& b)
{
    return a.second < b.second;
}

int solution(vector<int> food_times, long long k)
{
    // 다 먹을시간이 되는지 체크
    long long totalTimes = 0; 
    for (long long i=0; i<food_times.size(); i++) totalTimes += food_times[i];    
    if (totalTimes <= k) 
        return -1;

    // (테이블번호 : 먹는시간) 으로 map생성 후 오름차순 정렬
    vector<pair<long long, long long>> tableTimes;
    for (long long i=0; i<food_times.size(); i++)
    {
        tableTimes.push_back(make_pair(i, food_times[i]));
    }

    sort(tableTimes.begin(), tableTimes.end(), compare);
    
    long long currSize = food_times.size();

    
    long long i=0;
    long long currTimes = tableTimes[0].second;
    long long prevTime = currTimes;
    long long eatTimes = currSize * currTimes;
    
    while (k >= eatTimes)
    {
        k -= eatTimes;
        
        prevTime = tableTimes[i].second;
        while(currSize > 1 && i < food_times.size() && tableTimes[i].second == prevTime) 
        {
            i++;
            currSize--;
        }

        currTimes = tableTimes[i].second - prevTime;
        eatTimes = currSize * currTimes;
    }

    vector<long long> lastTable;
    for (long long tableIndex = i; tableIndex < food_times.size(); tableIndex++)
    {
        lastTable.push_back(tableTimes[tableIndex].first);
    }
    sort(lastTable.begin(), lastTable.end());


    int result = (lastTable[(k%lastTable.size())] + 1);

    return result;
}