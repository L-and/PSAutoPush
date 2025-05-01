#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main()
{
    int n;
    cin>>n;

    vector<int> nums(n);
    for(int i=0; i<n; i++)
        cin>>nums[i];

    stack<int> monoStack;
    vector<int> results(n);
    monoStack.push(-1);
    for(int i=n-1; i>=0; i--)
    {
        // monotonic stack의 decreasing 속성을 유지하기위해서 push를 하는 값보다 작은 값들은 제거 
        while (monoStack.top() <= nums[i])
        {   
            monoStack.pop();

            if (monoStack.size() == 0)
                break;
        }

        int nge = -1;
        if (monoStack.size() != 0)
            nge = monoStack.top();
            
        monoStack.push(nums[i]);

            results[i] = nge;
    }

    for(int result : results) cout<<result<<' ';

    return 0;
}