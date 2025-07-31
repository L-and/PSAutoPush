#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<vector<int>>> getRotateKey(vector<vector<int>>& key)
{
    int size = key[0].size();
    vector<vector<vector<int>>> newKeys(4,
    vector<vector<int>>(size, vector<int>(size, 0)));
    newKeys[0] = key;

    for (int keyIndex = 1; keyIndex < 4; keyIndex++)
    {
        vector<vector<int>> prevKey = newKeys[keyIndex-1];
        for(int j=0; j<size; j++)
        {
            for (int i=0; i<size; i++)
            {
                newKeys[keyIndex][j][i] = prevKey[size - 1 - i][j];
            }
        }
    }

    // for (int keyIndex = 0; keyIndex < 4; keyIndex++)
    // {
    //     for(int j=0; j<size; j++)
    //     {
    //         for (int i=0; i<size; i++)
    //         {
    //             cout << newKeys[keyIndex][j][i];
    //         }
    //         cout << endl;
    //     }
    //     cout << endl;
    // }

    return newKeys;
}

void expandLock(vector<vector<int>>& lock, int keySize)
{
    int n = lock.size();
    int newSize = n + 2 * (keySize - 1);

    vector<vector<int>> newLock(newSize, vector<int>(newSize, 0));

    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < n; i++)
        {
            newLock[j + keySize - 1][i + keySize - 1] = lock[j][i];
        }
    }

    lock = newLock;
}


bool openCheck(vector<vector<int>> key, vector<vector<int>>& lock)
{
    int start = key.size()-1;
    int end = lock.size() - key.size() + 1;

    for (int j=start; j<end; j++)
    {
        for (int i=start; i<end; i++)
        {
            if (lock[j][i] != 1) 
                return false;
        }
    }

    return true;
}

bool insertKey(vector<vector<int>>& key, vector<vector<int>> lock, int y, int x)
{
    // 열쇠를 적용한 lock배열 생성
    for (int j=0; j<key.size(); j++)
    {
        for (int i=0; i<key.size(); i++)
        {
            lock[y+j][x+i] += key[j][i];
        }
    }

    // 열린지(lock이 모두1인지) 확인
    return openCheck(key, lock);
}

bool tryOpen(vector<vector<int>> key, vector<vector<int>> lock)
{
    int end = lock.size() - key.size() + 1;
    
    vector<vector<int>> l = lock;
    for (int j=0; j<end; j++)
    {
        for (int i=0; i<end; i++)
        {
            bool isOpen = insertKey(key, lock, j, i);
            if (isOpen) return true;
        }
    }

    return false;
}



bool solution(vector<vector<int>> key, vector<vector<int>> lock) 
{
    // 90도씩 회전한 열쇠들을 생성
    vector<vector<vector<int>>> keys = getRotateKey(key);

    // (key크기-1)만큼 배열을 상,하,좌,우로 확장
    expandLock(lock, key.size());
    
    // 0 ~ (lock크기 - key크기)로 열쇠를 꼽을 기준점을 이동시키며 key를 꼽아봄
    for (auto key : keys)
    {
        if (tryOpen(key, lock))
            return true;
    }

    return false;
}

int main()
{
    cout << solution(
        {
            {0, 0, 1, 1}, 
            {0, 0, 0, 0}, 
            {0, 0, 0, 0},
            {0, 0, 0, 0}
        }, 
        {
            {1, 1, 1}, 
            {1, 0, 1},
            {1, 0, 1}
        }
    );

    return 0;
}