from collections import deque


n, m = map(int, input().split())

grid = []

for i in range(n):
    grid.append(list(map(int, input())))

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()
q.append([0, 0])
visited[0][0] = True

while q:
    y, x = q.popleft()
    # print(*grid,sep='\n')
    # print()
    # print(f"Current Pos: {y}{x}")
    # 큐에 방문할 좌표 추가
    for dy, dx in dir:
        new_y = y+dy
        new_x = x+dx

        # 범위검사

        if not (0<=new_x<m and 0<=new_y<n):
            continue

        # 방문검사 and 장애물 검사
        if not visited[new_y][new_x] and grid[new_y][new_x] != 0:
            q.append([new_y, new_x])
            
            visited[new_y][new_x] = True
            grid[new_y][new_x] += grid[y][x]

            # print(f"Queue Added: {new_y},{new_x} | d: {grid[new_y][new_x]}")

    

print(grid[n-1][m-1])