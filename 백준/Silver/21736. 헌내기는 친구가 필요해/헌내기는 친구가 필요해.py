from sys import stdin

n, m = map(int, stdin.readline().split())

campusMap = [[0] for _ in range(n)]
playerPos = []
friendsCnt = 0

for i in range(n):
    temp = list(stdin.readline())
    if 'I' in temp:
        playerPos = [i,temp.index('I')]
    campusMap[i] = temp
#---------------------------여까지 입력-------------------------------

# 벽이면 None, 아니면 이동한 좌표 뱉음
def move_and_check(pos: list, dir: list):
    x = pos[0] + dir[0]
    y = pos[1] + dir[1]

    if x < 0 or x >= n or y < 0 or y >= m: # 캠퍼스밖으로 나가지마라!
        return None

    if campusMap[x][y] == 'X':
        return None
    else:
        return [x,y]

dir_list = [[1,0],[0,1],[-1,0],[0,-1]]
visited = [[0]*m for _ in range(n)] # 방문한 좌표를 1, 아니면 0으로 x,y에 저장
pos_list = [playerPos.copy()] # 이동할 좌표들을 저장할 리스트

while len(pos_list) != 0:
    selected_pos = pos_list.pop() # 맨 위에 좌표를 선택

    if visited[selected_pos[0]][selected_pos[1]] != 1: # 방문한 좌표가 아니라면
        visited[selected_pos[0]][selected_pos[1]] = 1# 방문했다고 추가
    
    for dir in dir_list: # 4방향으로 이동한 좌표들 생성
        moved_pos = move_and_check(selected_pos, dir)

        # 방문 할 좌표가 캠퍼스안 and 방문 안한 장소라면 노드생성
        if moved_pos != None and visited[moved_pos[0]][moved_pos[1]] != 1:
            # print(visited)
            # print(moved_pos, moved_pos not in visited)
            pos_list.append(moved_pos)
            visited[moved_pos[0]][moved_pos[1]] = 1

            if campusMap[moved_pos[0]][moved_pos[1]] == 'P':
                friendsCnt += 1

if friendsCnt == 0:
    print("TT")
else:
    print(friendsCnt)