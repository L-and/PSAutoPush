from collections import deque

# m:가로, n:세로, h:높이
m, n, h = map(int, input().split())

box = [[[] for _ in range(n)] for _ in range(h)] # 박스에 토마토의 값을 저장(-1:비어있음, 0:안익음, 1:익음)
red_pos = [] # 익은 토마토의 위치를 저장하는 리스트
for z in range(h):
    for y in range(n):
        # 입력값 저장
        box[z][y] = list(map(int, input().split()))
        
for z in range(h):
    for y in range(n):
        for x in range(m):
            # 토마토의 위치 저장
            if box[z][y][x] == 1:
                red_pos.append([z, y, x])

# # 토마토가 익는 방향(아래, 위, 뒤, 앞, 좌, 우)
dir_list = [[-1,0,0], [1,0,0], [0,-1,0], [0,1,0], [0,0,-1], [0,0,1]]

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

queue = deque()
frist_red_toamtoes_pos = []
# 박스의 익은 토마토의 [z,y,x]값을 모두 큐에 추가 및 해당좌표를 방문처리
for pos in red_pos:
    
    red_z = pos[0]
    red_y = pos[1]
    red_x = pos[2]
    frist_red_toamtoes_pos.append([red_z, red_y, red_x])
    visited[red_z][red_y][red_x] = True

queue.append(frist_red_toamtoes_pos) # queue에 빨간 토마토의 값을 [[[z,y,x], [z,y,x]...]] 형태로 넣음

answer = -1 # 모든 토마토가 익는 일(day) 수
# BFS 1회당 box의 모든 익은 토마토의 좌표값을 2차원 리스트로 넣어서 1회:1일 로 카운트하게 구현
while True:
    red_tomatoes_pos = queue.popleft()

    # BFS를 해서 새로운 빨간 토마토의 좌표가 없다면 모든 토마토에 대해 처리가 끝났으므로 break
    if red_tomatoes_pos == []:
        break
    else:
        answer += 1

    new_red_tomatoes_pos = []
    for pos in red_tomatoes_pos:
        z = pos[0]
        y = pos[1]
        x = pos[2]

        # 다음 BFS depth때 익는 토마토들을 큐에 추가
        
        # pos의 토마토에서 dir방향의 토마토를 익게 만든 후 큐에 추가
        for dir in dir_list:
            new_z = z + dir[0]
            new_y = y + dir[1]
            new_x = x + dir[2]

            # 새로운 박스좌표의 범위검사 (범위 밖이면 다음 dir검사)
            if not(0<=new_x<m and 0<=new_y<n and 0<=new_z<h):
                continue

            # dir방향의 박스에 안익은 토마토가 있으면 익게(1) 만들고 new_red_tomatoes_pos에 추가
            if box[new_z][new_y][new_x] == 0 and not visited[new_z][new_y][new_x]:
                box[new_z][new_y][new_x] = 1
                
                new_red_tomatoes_pos.append([new_z, new_y, new_x])
                visited[new_z][new_y][new_x] = True

    queue.append(new_red_tomatoes_pos)
    

# 모든 토마토가 익은지 검사
all_tomatoes_red = True

for z in range(h):
    for y in range(n):
        for x in range(m):
            # 안 익은 토마토가 발견됨
            if box[z][y][x] == 0:
                all_tomatoes_red = False
                break;break;break

if all_tomatoes_red:
    print(answer)
else:
    print(-1)