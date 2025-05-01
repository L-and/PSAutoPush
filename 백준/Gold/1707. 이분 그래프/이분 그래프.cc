#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    int t,v,e;
    cin>>t;

    for(int _t=0;_t<t;_t++)
    {
        cin>>v>>e;

        vector<vector<int>> adj(v);

        for(int _e=0;_e<e;_e++)
        {
            int v1, v2;
            cin>>v1>>v2;
            
            v1-=1;
            v2-=1;
            adj[v1].push_back(v2);
            adj[v2].push_back(v1);
        }
        


        char color[20000] = {};
        // 정점이 어느 집합에 속하는지 'r', 'b'로 색 저장 (index = 정점번호)
        bool isBipartite = true; 
        // 이분 그래프로 가정 후 조건에 부합하지 않을경우 bfs 탈출을위한 플래그

        int vertex = 0; //탐색을 시작할 정점
        // 부분그래프가 있을 수 있으니 모든정점에 대해 검사
        while(vertex<v && isBipartite)
        {
            
            if(color[vertex] != '\0') 
            {
                vertex++;
                continue;
            }
            // BFS
            queue<int> q;
            q.push(vertex); // vertex번 정점부터 시작
            color[vertex] = 'b'; // vertex번 정점은 파란색으로 설정

            
            while(not q.empty() && isBipartite)
            {
                int pv;
                pv = q.front(); q.pop();


                //pv의 자식 정점(cv)들을 큐에 추가
                for(auto cv: adj[pv])
                {
                    // pv, cv 두 정점이 같은 색이라면 이분그래프가 아님
                    if(color[pv] == color[cv])
                    {
                        isBipartite = false;
                        break;
                    }
                    
                    // 색이 칠해지지 않은 정점을 큐에추가 및 색칠
                    if(color[cv] == '\0')
                    {
                        color[cv] = (color[pv] == 'b') ? 'r' : 'b';
                        q.push(cv);
                    }

                }
            }
            vertex++;
            
            // cout<<v<<' '<<isBipartite<<endl;
        }
        
        // cout<<"PRT";

        cout<<((isBipartite) ? "YES" : "NO")<<endl;
    }

    return 0;

}