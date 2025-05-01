#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

void dfs(vector<vector<int>> adjList, int v, vector<int> *t, bool *visited)
{
    t->push_back(v+1);
    
    sort(adjList[v].begin(), adjList[v].end());

    for(int child_v:adjList[v])
    {
        if(visited[child_v] == false)
        {
            visited[child_v] = true;
            dfs(adjList, child_v, t, visited);
        }
    }
}

void bfs(vector<vector<int>> adjList, int v, vector<int> *t, bool *visited)
{
    queue<int> q;
    q.push(v);
    visited[v] = true;

    while(not q.empty())
    {
        v = q.front(); q.pop();

        t->push_back(v+1);

        sort(adjList[v].begin(), adjList[v].end());

        for(int child_v: adjList[v])
        {
            if(visited[child_v] == false)
            {
                visited[child_v] = true;
                q.push(child_v);
            }
        }
    }
}

int main()
{
    int n,m,v;
    cin>>n>>m>>v;

    vector<vector<int>> adjList(n);

    int v1, v2;
    for(int _=0;_<m;_++)
    {
        cin>>v1>>v2;

        adjList[v1-1].push_back(v2-1);
        adjList[v2-1].push_back(v1-1);
    }

    vector<int> trace;
    bool visited[n];
    for(int i=0;i<n;i++) visited[i] = false;
    visited[v-1]=true;
    dfs(adjList, v-1, &trace, &visited[0]);
    for(int val:trace)
        cout<<val<<' ';
    cout<<endl;

    trace.clear();
    for(int i=0;i<n;i++) visited[i] = false;
    bfs(adjList, v-1, &trace, &visited[0]);
    for(int val:trace)
        cout<<val<<' ';
    cout<<endl;
}