#include <iostream>
#include <queue>
#include <algorithm>
#include <map>
using namespace std;

int main()
{
    long long startNum, targetNum;

    cin >> startNum >> targetNum;

    int result = -1;
    bool findFlag = false;

    queue<pair<long long, int>> q;

    q.push(make_pair(startNum, 1));

    while (q.size() != 0)
    {
        auto curPair = q.front(); q.pop();
        long long curNum = curPair.first;
        int curCnt = curPair.second;

        // cout << curNum << ", " << curCnt << endl;

        if (curNum == targetNum)
        {
            result = curCnt;
            break;
        }

        // 새로운 숫자를 큐에 추가
        long long num1 = (curNum * 2);
        long long num2 = (curNum * 10 + 1);
        if (num1 <= targetNum)
        {
            q.push(make_pair(num1, curCnt+1));
        }

        if (num2 <= targetNum)
        {
            q.push(make_pair(num2, curCnt+1));
        }
    }

    cout << result;

    return 0;
}