#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// WBWBWB, BWBWBW의 2차원 체스판이지만 1차원으로 바꿔도
// x+y의 값이 1 증가할떄마다 칸의 색깔이 바뀌어야하므로 px, py가 W, B로 가정하고
// 8x8칸을 탐색하며 두 케이스와 다른값인 칸의 개수를 세어줌
int getMinResult(vector<vector<char>>& graph, int pX, int pY)
{
    int cntW = 0;
    int cntB = 0;
    for(int y=0;y<8;y++)
    {
        for(int x=0;x<8;x++)
        {
            if((x+y)%2 == 0) // 짝수번째 칸
            {
                if(graph[pY+y][pX+x] != 'W') // px, py칸이 W인 경우
                {
                    cntW++;
                }

                if(graph[pY+y][pX+x] != 'B') // px, py칸이 B인 경우
                {
                    cntB++;
                }
            }
            else // 홀수번째 칸
            {
                if(graph[pY+y][pX+x] != 'B') // px, py칸이 W인 경우
                {
                    cntW++;
                }

                if(graph[pY+y][pX+x] != 'W') // px, py칸이 B인 경우
                {
                    cntB++;
                }
            }
        }
    }

    return min(cntW, cntB);
}

int main()
{
    int n,m;

    cin>>n>>m;

    vector<vector<char>> graph(n, vector<char>(m,0));

    for(int y=0; y<n; y++)
    {
        for(int x=0; x<m; x++)
        {
            cin>>graph[y][x];
        }
    }

    int result = INT_MAX;
    for(int y=0; y<n-7; y++)
    {
        for(int x=0; x<m-7; x++)
        {
            result = min(result, getMinResult(graph, x, y));
        }
    }

    cout<<result;

    return 0;
}