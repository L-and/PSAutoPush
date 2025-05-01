#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

void dfs(int n, vector<char>& symbol, bool* used, vector<int>& result, int k)
{
    if(result.size() >= (k+1))
    {
        // cout<<"## Result: ";
        // for(auto v: result) // cout<<v;
        // cout<<endl;
        return;
    } 
    
    char curSymbol = symbol[result.size()-1];

    // cout<<"######"<<endl;
    // for(auto v: result)  cout<<v;
    // cout<<endl;
    // cout<<"SYMBOL"<<curSymbol<<endl;
    
    int newN = -1;
    if(curSymbol == '<')
    {
        for(int num=n+1; num<=9; num++)
        {
            if(used[num] == false)
            {
                used[num] = true;
                newN = num;
                
                result.push_back(newN);

                dfs(newN, symbol, used, result, k);

                if(result.size() >= (k+1)) break;

                result.pop_back();
                used[newN] = false;
            }
        }
    }
    else if(curSymbol == '>')
    {
        for(int num=n-1; num>=0; num--)
        {
            if(used[num] == false)
            {
                used[num] = true;
                
                newN = num;

                result.push_back(newN);
                dfs(newN, symbol, used, result, k);

                if(result.size() >= (k+1)) break;

                result.pop_back();
                used[newN] = false;
            }
        }
    }
}

int main()
{
    int k=0;
    cin>>k;
    
    vector<char> symbol(k); // 부등호
    vector<vector<bool>> unableNums(k+1, vector<bool>(false, 10)); // unableNums[숫자의 위치] = {0~9까지 사용가능한지 여부}

    for(int i=0; i<k; i++) cin>>symbol[i];

    vector<int> result;
    
    for(int num=9; num>=0; num--)
    {
        
        bool used[10] = {false};

        result.push_back(num);
        used[num] = true;
        dfs(num, symbol, used, result, k);

        if(result.size() == (k+1)) break;
        else    result.clear();
    }

    for(auto v: result) cout<<v;
    
    cout<<endl;
    result.clear();
    for(int num=0; num<10; num++)
    {
        
        bool used[10] = {false};

        result.push_back(num);
        used[num] = true;
        dfs(num, symbol, used, result, k);

        if(result.size() == (k+1)) break;
        else    result.clear();
    }

    for(auto v: result) cout<<v;

    

    return 0;
}