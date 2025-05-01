#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin>>n;

    vector<int> p(n); // 대기시간
    
    for(int i=0; i<n; i++) cin>>p[i];
    
    // 오름차순으로 정렬
    sort(p.begin(), p.end());

    // 최소 총대기시간은 대기시간을 오름차순으로 정렬 후 sum(i의 대기시간)
    // i의 대기시간은 i-1번째 사람의 대기시간 + i번쨰사람의 대기시간
    
    int waitTime = 0; // i에서의 대기시간
    int result = 0; // 총 대기시간
    

    for(int i=0; i<p.size(); i++)
    {
        waitTime += p[i];
        result += waitTime;
    }

    cout << result;
}