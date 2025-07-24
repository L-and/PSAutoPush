#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool compareByTime(const pair<int, int>& a, const pair<int, int>& b)
{
    return a.second < b.second;
}

int solution(vector<int> food_times, long long k)
{
    long long totalTime = 0;
    for (int t : food_times) totalTime += t;
    if (totalTime <= k) return -1;

    int n = food_times.size();

    // (index, time) 쌍 정렬
    vector<pair<int, int>> food;
    for (int i = 0; i < n; ++i)
        food.emplace_back(i, food_times[i]);

    sort(food.begin(), food.end(), compareByTime);

    long long prevTime = 0;
    int idx = 0;
    int remaining = n;

    while (idx < n)
    {
        long long currTime = food[idx].second;
        long long diff = currTime - prevTime;
        long long consume = diff * remaining;

        if (k < consume) break;

        k -= consume;
        prevTime = currTime;

        // upper_bound로 다음 group 위치 찾기
        auto it = upper_bound(food.begin() + idx, food.end(), currTime,
            [](int value, const pair<int, int>& p) {
                return value < p.second;
            });

        int nextIdx = it - food.begin();
        remaining -= (nextIdx - idx);
        idx = nextIdx;
    }

    // 남은 음식들 원래 인덱스 기준 정렬
    vector<int> result;
    for (int i = idx; i < n; ++i)
        result.push_back(food[i].first);
    sort(result.begin(), result.end());

    return result[k % result.size()] + 1;
}
