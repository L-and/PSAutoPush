#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <memory>
using namespace std;

template <typename T>
void printVector2D(vector<vector<T>> &adj, string comment)
{
    cout << comment << endl;
    for (const auto &rows : adj)
    {
        for (const auto &val : rows)
        {
            cout << val << ' ';
        }
        cout << endl;
    }
    cout << endl;
}

bool isEmpty(pair<int, int> p)
{
    return (p.first == -1 && p.second == -1);
}

// 추가할 위치의 [y,x]좌표를 범위초과계산 후 생성
vector<pair<int, int>> getNewpos(int y, int x, int n, int m)
{
    static const vector<pair<int, int>> directions = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    vector<pair<int, int>> newposVector;
    for (const auto &dir : directions)
    {
        int new_x = x + dir.second;
        int new_y = y + dir.first;

        if (new_y >= 0 && new_y < n && new_x >= 0 && new_x < m)
        {
            newposVector.push_back({new_y, new_x});
        }
    }

    return newposVector;
}

// icePos: 없을경우 {-1, -1} return
pair<int, int> getIcePos(vector<vector<int>> &adj, vector<vector<bool>> &visited, int& n, int& m)
{
    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < m; col++)
        {
            if (adj.at(row).at(col) > 0 && (!visited.at(row).at(col)))
            {
                return {row, col};
            }
        }
    }

    return {-1, -1};
}

// BFS를 사용해 빙산의 개수 계산
int getIcebergCnt(vector<vector<int>> &adj, int& n, int& m)
{
    int icebergCnt = 0;
    // 얼음의 위치
    pair<int, int> icePos;

    vector<vector<bool>> visited(n, vector<bool>(m, false));

    // 빙산의 개수 계산
    icePos = getIcePos(adj, visited, n, m);
    while (!isEmpty(icePos))
    {
        icebergCnt++;

        queue<pair<int, int>> q;

        visited.at(icePos.first).at(icePos.second) = true;
        q.push(icePos);

        while (!q.empty())
        {
            auto pos = q.front();
            q.pop();

            for (auto newPos : getNewpos(pos.first, pos.second, n, m))
            {
                int x, y;
                x = newPos.second;
                y = newPos.first;

                if ((adj.at(y).at(x) > 0) && (!visited.at(y).at(x)))
                {
                    visited.at(y).at(x) = true;
                    q.push({y, x});
                }
            }
        }

        icePos = getIcePos(adj, visited, n, m);
    }

    return icebergCnt;
}

int main()
{
    int n, m;
    cin >> n >> m;

    // 각 빙산의 녹기까지의 시간을 저장
    vector<vector<int>> adj(n, vector<int>(m, 0));

    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < m; col++)
        {
            cin >> adj.at(row).at(col);
        }
    }

    // 1. 칸의 녹는속도 계산(인접한 0의개수, 단 이전에 0이된 칸은 포함X)
    // 2. 인접한 칸을 큐에추가

    #pragma region PS

    int year = 0;

    queue<pair<int, int>> q;
    vector<vector<bool>> v(n, vector<bool>(m, false));

    auto oldAdj = make_shared<vector<vector<int>>>(adj); // 루프 전 adj
    auto newAdj = make_shared<vector<vector<int>>>(n, vector<int>(m, 0)); // 루프 후 adj

    int icebegCnt = getIcebergCnt(*oldAdj, n, m);
    pair<int, int> icePos = getIcePos(*oldAdj, v, n, m);

    // 빙산의 1인동안 계속 진행
    while (icebegCnt == 1)
    {
        // cout<<"얼음의 위치";
        // cout<<icePos.first<<' '<<icePos.second<<endl;
        // printVector2D(*oldAdj, "맵 상태");
        // cout<<"빙산 개수: "<<icebegCnt<<endl;0

        year++; // 년도 증가

        q.push(icePos);
        v.at(icePos.first).at(icePos.second) = true;

        // 얼음 녹이기 계산: BFS
        while (!q.empty())
        {
            pair<int, int> pos = q.front();
            q.pop();

            int x, y;
            x = pos.second;
            y = pos.first;

            int meltCnt = 0;
            // pos의 얼음녹이기 및 새로운 얼음좌표를 큐에 추가
            for (auto newPos : getNewpos(y, x, n, m))
            {
                int newX = newPos.second;
                int newY = newPos.first;

                // pos 주변의 바다(0) 카운트
                if (oldAdj->at(newY).at(newX) == 0)
                    meltCnt++;

                // 새로운 얼음좌표를 큐에 추가
                if (!v.at(newY).at(newX) && oldAdj->at(newY).at(newX) != 0)
                {
                    v.at(newY).at(newX) = true;
                    q.push({newY, newX});
                }
            }

            // pos 녹인값을 저장
            newAdj->at(y).at(x) = max(0, (oldAdj->at(y).at(x) - meltCnt));
        }

        // 방문값 초기화
        for (int i = 0; i < n; i++)
            fill(v.at(i).begin(), v.at(i).end(), false);

        // 얼음이 녹은 뒤 빙산갯수 계산
        icebegCnt = getIcebergCnt(*newAdj, n, m);


        // 얼음의 위치찾기
        icePos = getIcePos(*newAdj, v, n, m);

        // adj 갱신
        swap(oldAdj, newAdj); // 새로운 상태값을 adj로 지정
        newAdj = make_shared<vector<vector<int>>>(n, vector<int>(m, 0)); // newAdj 초기화
    }

    if(icebegCnt == 0) year = 0;

    cout << year;

    #pragma endregion
    
    return 0;
}
