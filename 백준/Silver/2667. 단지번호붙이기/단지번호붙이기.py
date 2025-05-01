from collections import deque

def bfs(x, y):

    num_of_house = 0

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 4방향 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 집이 없는곳이라면 continue
            if graph[nx][ny] == 0:
                continue

            #  수를 안센 집이라면
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                num_of_house += 1
                queue.append((nx, ny))

    return num_of_house


n = int(input())

graph = []
visited = [[False for col in range(n)] for row in range(n)]
numOfHouseList = []
result = 0

for i in range(n):
    graph.append(list(map(int, input())))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] != True:
            numOfHouseList.append(bfs(i, j))
            result += 1

numOfHouseList.sort()

print(result)

for i in range(len(numOfHouseList)):
    if numOfHouseList[i] == 0:
        print(1)
    else:
        print(numOfHouseList[i])