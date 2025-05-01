from collections import deque

n = int(input())
colors = [[] for _ in range(n)]


for y in range(n):
    colors[y] = list(input())

dir = [[-1,0],[1,0],[0,-1],[0,1]]


def bfs(pos, v):
    q.append(pos)
    v[pos[0]][pos[1]] = True

    while q:
        y, x = q.popleft()
        cur_c = colors[y][x]

        for d in dir:
            new_x = x + d[1]
            new_y = y + d[0]

            if (0<=new_x<n and 0<=new_y<n) and (not v[new_y][new_x]) and cur_c == colors[new_y][new_x]: # visited Check
                q.append([new_y, new_x])
                v[new_y][new_x] = True
                


def get_area_cnt(is_RGblind):
    v = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0

    # 적록색약인 경우 입의 G을 R로 변경
    if is_RGblind:
        for y in range(n):
            for x in range(n):
                if colors[y][x] == 'G':
                    colors[y][x] = 'R'

    for y in range(n):
        for x in range(n):
            if not v[y][x]:
                bfs([y,x], v)
                cnt += 1
    
    return cnt

q = deque()
print(get_area_cnt(False), get_area_cnt(True))