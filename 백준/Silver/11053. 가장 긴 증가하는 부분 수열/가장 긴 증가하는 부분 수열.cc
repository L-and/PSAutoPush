#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin>>n;
    
    vector<int> nums(n);
    for(int& num: nums) cin>>num;

    // A[0] ~ A[n]까지 반복하며
    // A[i]가 result[j]보다 작고 result[j]가 최대인 위치를 찾아 바꿔나가면 result의 길이가 정답 
    vector<int> result(1, nums[0]);

    for(int num: nums)
    {
        // cout<<result.back();
        if(num > result.back()) result.push_back(num);
        else
        {
            // result에 num과 대체가능한 수의 위치 검색
            int start=0;
            int end=result.size();

            while(start<end)
            {
                int mid = (start+end) / 2;
                
                if(result[mid] >= num) end = mid;
                else if(result[mid] < num) start = mid+1;
            }

            result[end] = num;
        }

    }
    

    cout<<result.size();

    return 0;
}