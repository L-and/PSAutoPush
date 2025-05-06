#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
vector<int> nums;


void solve(vector<int>& selectedIndexes, int start)
{
    if (selectedIndexes.size() == m)
    {
        for(int& i : selectedIndexes) cout << nums[i] << ' ';
        cout << '\n';
        return;
    }

    int prevNum = -1;
    for(int i=start; i<nums.size(); i++)
    {
        if (prevNum == nums[i]) continue;
        
        selectedIndexes.push_back(i);
        solve(selectedIndexes, i);
        selectedIndexes.pop_back();

        prevNum = nums[i];
    }
}

int main()
{
    cin >> n >> m;

    nums.resize(n);
    for(int& num : nums) cin >> num;

    sort(nums.begin(), nums.end());

    vector<int> selectedIndexes;
    solve(selectedIndexes, 0);

    return 0;
}