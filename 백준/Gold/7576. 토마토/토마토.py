from collections import deque

n, m = map(int, input().split())

tomato = [[] for i in range(m)]
red_tomatoes = [] # 익은 토마토의 위치를 저장하는 리스트

for i in range(m):
    # 입력값 저장
    tomato[i] = list(map(int, input().split()))

for i in range(m):
    for j in range(n):
        # 토마토의 위치 저장
        if tomato[i][j] == 1:
            red_tomatoes.append([i, j])

# 토마토가 익는 방향
dir_list = [[-1,0], [1,0], [0,-1], [0,1]]

queue = deque()
queue.append(red_tomatoes)
red_tomatoes = []



answer = 0
while queue:
    red_tomatoes = queue.popleft()

    next_red_tomatoes = list()
    for red_tomato in red_tomatoes:
        for dir in dir_list:
            new_x = red_tomato[0] + dir[0]
            new_y = red_tomato[1] + dir[1]
            
            # 박스의 범위(n, m)이내인지 확인, [new_x, new_y]가 익은 토마토인지 확인 후 익는 토마토 추가
            if (0<=new_x<m and 0<=new_y<n) and tomato[new_x][new_y] == 0:
                tomato[new_x][new_y] = 1
                next_red_tomatoes.append([new_x,new_y])
            else:
                continue

    if next_red_tomatoes != []:
        queue.append(next_red_tomatoes) # 다음 loop에서 익는 토마토의 위치를 큐에 추가
        answer += 1

done = True
for i in range(m):
    for j in range(n):
        # 토마토의 위치 저장
        if tomato[i][j] == 0:
            done = False
            break;break
        
if done:
    print(answer)
else:
    print(-1)