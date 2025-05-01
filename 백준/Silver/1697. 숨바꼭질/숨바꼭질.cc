#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> createNewNodes(int n)
{
    vector<int> newNodes;

    if(n-1>=0)  newNodes.push_back(n-1);
    if(n+1<=100000) newNodes.push_back(n+1);
    if(n*2<=100000) newNodes.push_back(n*2);

    return newNodes;
}

int main()
{
    int n, k;
    cin>>n>>k;

    queue<vector<int>> q;

    vector<int> tmp;
    tmp.push_back(n);

    q.push(tmp);

    int time = -1;

    bool isDone = false;
    vector<bool> visited(100001, false);
    while(not isDone)
    {
        time++;
        vector<int> currentDepth = q.back(); q.pop();

        vector<int> newDepth;
        
        // cout<<"# DEPTH"<<time<<endl;
        for(int val : currentDepth)
        {
            // cout<<val<<endl;
            if(val == k) 
            {
                isDone = true;
                break;
            }
            else
                for(int newV : createNewNodes(val))
                {
                    if(not visited[newV])
                    {
                        visited[newV] = true;
                        newDepth.push_back(newV);
                    }
            }
        }
        q.push(newDepth);
        
    }

    cout<<time;
}