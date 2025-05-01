#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 1. 점들과 각 선분의 시작점을 오름차순으로 정렬
// 2. 선분의 시작점보다 작거나 같은 인덱스, 끝점보다 크거나 같은 인덱스를 구해 두 인덱스의 차 +1이
// 해당 선분에 포함되는 점 개수
// 3. 인덱스 위치를 이분탐색으로 찾기
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int v_cnt, edge_cnt;
    cin>>v_cnt>>edge_cnt;

    vector<int> v_list(v_cnt, 0);
    vector<vector<int>> edge_list(edge_cnt, vector<int>(2,0));

    for(int i=0;i<v_cnt;i++) cin>>v_list[i];
    for(int i=0;i<edge_cnt;i++) cin>>edge_list[i][0]>>edge_list[i][1];

    // 여기까지가 입력

    vector<int> result_list; // 선분위의 점들의 개수를 저장할 변수

    sort(v_list.begin(), v_list.end());


    //이분탐색 시작
    int start, end, mid;

    for(vector<int> edge: edge_list)
    {
        int edge_s=edge[0];
        int edge_e=edge[1];

        int first_index, last_index;
        
        // 점 리스트에 선분의 시작점보다 작은값의 인덱스 찾기
        start=0,end=v_cnt-1;
        while(start<=end)
        {
            mid = (start+end)/2;

            if(v_list[mid] < edge_s)
            {
                start = mid+1;
            }
            else
            {
                end = mid-1;
            }
        }
        first_index = start;

        // 점 리스트에 선분의 끝점보다 큰 인덱스 찾기
        start=0,end=v_cnt-1;
        while(start<=end)
        {
            mid = (start+end)/2;

            if(v_list[mid] > edge_e)
            {
                end = mid-1;
            }
            else
            {
                start = mid+1;
            }
        }
        last_index = end;
        
        result_list.push_back(last_index-first_index+1);
    }

    for(int result: result_list) cout<<result<<'\n';

    return 0;
}