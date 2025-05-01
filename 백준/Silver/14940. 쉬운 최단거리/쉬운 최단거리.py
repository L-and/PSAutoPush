from enum import Enum
from collections import deque
# start_pos에서 dir 방향으로 이동 후 이전좌표의 distance_map[i][j] + 1을 distance_map에 저장하는 방식으로 BFS진행


# 이동가능
class LandType(Enum):
    NOT_VISIT = -1
    BLOCKED = 0
    WALKABLE = 1
    TARGET = 2

# 이동가능한 4방향(좌,하,우,상)
dir_list = [[0, -1], [1, 0], [0, 1], [-1, 0]]

# n: 가로, m:세로 크기
n, m = map(int, input().split())

terrain_map  = [0 for _ in range(n)] # 지도에 대한 정보
distance_map = [[LandType.NOT_VISIT.value for _ in range(m)] for _ in range(n)] # 각 좌표에 대한 TARGET까지 거리정보

start_pos = [] # TARGET 좌표

for i in range(n):
    # 입력데이터 처리
    terrain_map[i] = list(map(int, input().split()))

for i in range(n):
    # TARGET지점의 좌표저장
    if LandType.TARGET.value in terrain_map[i]:
        start_pos = [i, terrain_map[i].index(LandType.TARGET.value)]

queue = deque()

queue.append(start_pos)
distance_map[start_pos[0]][start_pos[1]] = 0 # 시작지점의 distance_map 값 설정

while queue:
    current_pos = queue.popleft()
    x = current_pos[0]
    y = current_pos[1]


    # current_pos로부터 4방향으로 방문체크(distance_map[new_pos] == LandType.NOT_VISIT 인지 확인) 후 큐에 추가 및 distance_map 업데이트
    for dir in dir_list:
        new_x = x + dir[0]
        new_y = y + dir[1]

        # 새로운 좌표가 범위를 벗어난 경우 다음dir을 계산하도록 continue 처리
        if 0<=new_x<n and 0<=new_y<m:
            pass
        else:
            continue
        
        # 방문검사, 이동가능검사(new_pos, current_pos 체크)
        if distance_map[new_x][new_y] == LandType.NOT_VISIT.value and terrain_map[new_x][new_y] == LandType.WALKABLE.value and terrain_map[x][y] >= LandType.WALKABLE.value:
            queue.append([new_x, new_y]) # 추후 방문할 큐에 좌표값 추가
            distance_map[new_x][new_y] = distance_map[x][y] + 1 # map[x,y] + 1로 이동거리 증가
        # BLOCKED이면 distance_map에 0으로 저장
        # elif distance_map[new_x][new_y] == LandType.NOT_VISIT.value and terrain_map[new_x][new_y] == LandType.BLOCKED.value:
        #     distance_map[new_x][new_y] = 0
        #     queue.append([new_x, new_y]) # distance_map을 업데이트하기위해 
        # 도달할 수 없는 위치(-1)은 distance_map 초기값이니 자동으로 계산됨
            
for i in range(n):
    for j in range(m):
        if terrain_map[i][j] == LandType.BLOCKED.value:
            distance_map[i][j] = 0


# 결과 출력
for i in range(n):
    print(*distance_map[i])