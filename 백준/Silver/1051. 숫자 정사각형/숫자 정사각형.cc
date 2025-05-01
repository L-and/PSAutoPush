#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int n, m;

    cin>>n>>m;

    map<pair<int, int>, vector<int>> dict; // 숫자의 인덱스를 저장하는 딕셔너리 [row, number] = [col1, col2, ...]
    string numChar;
    for(int row=0; row<n; row++)
    {   
        cin>>numChar;

        for(int col=0;col<numChar.size(); col++)
        {
            int num = int(numChar[col])-'0';

            pair<int, int> key(row, num); // [row, num]을 키로사용
            if(dict.count(key)) // 키가 dict에 존재
            {
                dict[key].push_back(col);
            }
            else
            {
                dict[key] = vector<int>(1, col);
            }
        }
        
    }
    int maxSize = 1;
    // for(auto it = dict.begin(); it != dict.end(); it++)
    // {
    //     cout<<"ROW: "<<(it->first.first)<<',';
    //     cout<<"NUM: "<<(it->first.second)<<endl;
    //     for(auto num: it->second)
    //     {
    //         cout<<num<<' ';
    //     }
    //     cout<<endl;
    // }
    
    for(auto it = dict.begin(); it!=dict.end(); it++)
    {
        int curRow = it->first.first;
        int num = it->first.second;

        vector<int>& idxV = it->second;
        
        // 왼쪽 col값과 오른쪽 col값을 만들어 만들어질 수 있는 사각형의 최대크기를 계산
        for(int leftColIndex=0; leftColIndex<idxV.size(); leftColIndex++)
        {
            int leftCol = idxV[leftColIndex];
            for(int rightColIndex=leftColIndex+1; rightColIndex<idxV.size(); rightColIndex++)
            {
                int rightCol = idxV[rightColIndex];

                for(int row=curRow+1; row<n; row++)
                {
                    pair<int, int> tmpPair(row, num);

                    // curRow 이외 row의 num을 찾았으면 인덱스를 검사해 사각형인지 검사
                    if(dict.find(tmpPair) != dict.end())
                    {
                        vector<int>& tmpV = dict[tmpPair];
                        auto leftIt = find(tmpV.begin(), tmpV.end(), leftCol);
                        auto rightIt = find(tmpV.begin(), tmpV.end(), rightCol);

                        if((leftIt != tmpV.end()) && (rightIt != tmpV.end()))
                        {
                            int w = (rightCol - leftCol + 1);
                            int h = (row - curRow + 1);
                            // cout<<"Width: "<<w<<" / Height: "<<h<<" / SIZE: "<<w*h<<endl;
                            if(w==h)
                                maxSize = max(maxSize, w*h);
                        }
                    }
                }

            }
        }

        
    }
    cout<<maxSize;
    return 0;
}