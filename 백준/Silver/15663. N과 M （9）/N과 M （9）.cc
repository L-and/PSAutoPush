#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve(int m, vector<int>& nums, vector<int>& result, vector<bool>& visited)
{
    if (result.size() == m)
    {
        for (auto& index : result) cout << nums[index] << " ";
        cout << "\n";
        return;
    }

    // result에 동일한 숫자를 제거하기위해 이전숫자 저장
    int prev = -1;
    for(int i=0; i<nums.size(); i++)
    {
        int& num = nums[i];

        // result에 동일한 index값을 안넣기위해 검사
        if (visited[i] || num == prev) continue;

        visited[i] = true;
        result.push_back(i);
        solve(m, nums, result, visited);
        result.pop_back();
        visited[i] = false;

        prev = num; 
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> nums(n);

    for(auto& num : nums) 
    {
        cin >> num;
    }
    sort(nums.begin(), nums.end());

    vector<int> result; // 결과 조합들을 저장
    vector<bool> visited(n, false);

    solve(m, nums, result, visited);

    return 0;
}