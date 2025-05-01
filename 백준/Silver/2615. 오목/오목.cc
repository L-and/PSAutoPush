#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int board_size = 19;

class Pos
{
    public:
    int x;
    int y;

    Pos()
    {
        x = -1; y = -1;
    }
    Pos(int _x, int _y)
    {
        x = _x; y = _y;
    }

    // 범위검사
    bool safe()
    {
        if((x>=0 && x<board_size) && (y>=0 && y<board_size))
            return true;

        return false;
    }

    // equal
    bool operator==(const Pos& p) const
    {
        if((x == p.x) && (y == p.y)) return true;
        else return false;
    }

    // not equal
    bool operator!=(const Pos& p) const
    {
        if((x == p.x) && (y == p.y)) return false;
        else return true;
    }
};

// _pos가 posList에 있는지 검사 및 제거하는 함수 (제거는 방문검사를 위해)
bool popPos(Pos& _pos, vector<Pos>& posList)
{
    for(auto it=posList.begin(); it!=posList.end(); it++)
    {
        if(*it == _pos)
        {
            posList.erase(it);
            return true;
        }
    }

    return false;
}

// 오목완성시 ture반환 및 winnerPos 첫위치 저장
bool checkWin(vector<vector<int>>& board, vector<Pos>& originPosList,vector<Pos>& dirList, Pos& winnerPos)
{
    for(auto dir: dirList)
    {
        // cout<<endl<<"방향: "<<dir.x<<' '<<dir.y<<endl;
        // posList에서 pop해가며 pop된 pos의 +,- dir로 검사해가며 count를 계산
        vector<Pos> posList = originPosList;
        
        
        while(!posList.empty())
        {
            int cnt=0;
            queue<Pos> q;

            Pos startPos = posList.front();
            q.push(posList.front());
            posList.erase(posList.begin());

            // cout<<"검사시작 좌표: ";
            // cout<<winnerInfo.second.y+1<<' '<<winnerInfo.second.x+1;

            while(!q.empty())
            {
                cnt++;
                Pos current = q.front(); q.pop();

                //가장 왼쪽돌의 좌표를 저장
                if(startPos.x > current.x) startPos = current;

                // 현재위치의 -,+dir 방향의 좌표
                Pos prev(current.x - dir.x, current.y - dir.y);
                Pos next(current.x + dir.x, current.y + dir.y);

                // 범위검사 and 방문검사
                if(prev.safe() && popPos(prev, posList))
                {
                    q.push(prev);
                }

                if(next.safe() && popPos(next, posList))
                {
                    q.push(next);
                }
            }
            // cout<<"> "<<cnt<<endl;
            if(cnt==5)
            {
                winnerPos = startPos;
                return true;
            }

        }
    }

    return false;
}

int main()
{
    vector<vector<int>> board(board_size, vector<int>(board_size, 0));
    vector<Pos> whitePosList;
    vector<Pos> blackPosList;

    // 입력받기
    for(int y=0; y<board_size; y++)
    {
        for(int x=0; x<board_size; x++)
        {
            cin>>board[y][x];

            if(board[y][x] == 1) // 검은돌
                blackPosList.push_back(Pos(x, y));
            else if(board[y][x] == 2)
                whitePosList.push_back(Pos(x, y));
        }
    }

    // 검사할 방향
    vector<Pos> dirList(4);
    dirList[0] = Pos(1, -1);
    dirList[1] = Pos(1, 0);
    dirList[2] = Pos(1, 1);
    dirList[3] = Pos(0, 1);

    bool whiteWin = false;
    bool blackWin = false;

    // 승자의 정보를 {돌, {x, y}}로 저장

    Pos winnerPos = Pos();

    blackWin = checkWin(board, blackPosList, dirList, winnerPos);

    whiteWin = checkWin(board, whitePosList, dirList, winnerPos);

    if(winnerPos == Pos())
    {
        cout<<'0'<<endl;
    }
    else
    {
        cout<<((blackWin) ? '1' : '2')<<endl;
        cout<<winnerPos.y+1<<' '<<winnerPos.x+1;
    }

    return 0;
    
}
