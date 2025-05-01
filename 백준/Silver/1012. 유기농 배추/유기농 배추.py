import collections
import sys

def bfs(napa_pos_list, width, height):
    # map = [[0 for i in range(height)] for j in range(width)]


    # for pos in napa_pos_list:
    #     map[pos[0]][pos[1]] = 1

    count = 0
    dir_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    queue = collections.deque()
    
    visited_pos = [[False for i in range(height)] for j in range(width)]

    while len(napa_pos_list) != 0:
        node = napa_pos_list.pop()

        if visited_pos[node[0]][node[1]] != True:
            queue.append(node)
        else:
            continue

        while len(queue) != 0: # 큐가 빌때까지 반복
            node = queue.popleft()
            visited_pos[node[0]][node[1]] = True

            # 선택된 노드의 상하좌우의 노드 총 4개를 생성에 큐에 추가
            for dir in dir_list:
                near_pos = [node[0] + dir[0], node[1] + dir[1]]

                # 범위를 벗어난경우 위치 조정
                if near_pos[0]>= width-1:
                    near_pos[0] = width-1
                elif near_pos[0] < 0:
                    near_pos[0] = 0

                if near_pos[1]>= height-1:
                    near_pos[1] = height-1
                elif near_pos[1] < 0:
                    near_pos[1] = 0

                if not visited_pos[near_pos[0]][near_pos[1]] and near_pos in napa_pos_list and not near_pos in queue:
                    queue.append(near_pos)

        count += 1

    return count

t = int(input())

for _ in range(t):
    width, height, napa_cnt = map(int, sys.stdin.readline().split())
    napa_pos_list = []

    for i in range(napa_cnt):
        napa_pos_list.append(list(map(int, sys.stdin.readline().split())))

    print(bfs(napa_pos_list, width, height))

