#include <iostream>
#include <queue>
#include <algorithm>
#include <map>
using namespace std;

int main()
{
    int startNum, targetNum;

    cin >> targetNum >> startNum;

    int result = -1;
    bool findFlag = false;

    queue<pair<int, int>> q;

    q.push(make_pair(startNum, 1));

    while (q.size() != 0)
    {
        auto curPair = q.front(); q.pop();
        int curNum = curPair.first;
        int curCnt = curPair.second;

        if (curNum == targetNum)
        {
            result = curCnt;
            break;
        }

        // 새로운 숫자를 큐에 추가
        int num1 = (curNum / 2);
        int num2 = ((curNum - 1) / 10);
        if ((curNum % 2 == 0) && num1 >= targetNum)
        {
            q.push(make_pair(num1, curCnt+1));
        }

        if ((curNum % 10 == 1) && num2 >= targetNum)
        {
            q.push(make_pair(num2, curCnt+1));
        }
    }

    cout << result;

    return 0;
}