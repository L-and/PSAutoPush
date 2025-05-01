from collections import deque

mat = [0 for _ in range(100)]

n, m = map(int, input().split())

for _ in range(n):
    ladder_i, target_i = map(int, input().split())
    mat[ladder_i-1] = target_i -1

for _ in range(m):
    snake_i, target_i = map(int, input().split())
    mat[snake_i-1] = target_i -1


visited = [False for _ in range(100)]
q = deque()
# 첫번째 칸을 시작노드로 설정, 각 노드에 몇번의 주사위 굴림이 있었는지를 저장
# [num, count]
q.append([0, 0])
visited[0] = True

# 1번칸과 100번칸은 뱀,사다리로 이동불가
answer = 0
while q:
    node = q.popleft()
    num = node[0]
    cnt = node[1]

    # 100번째 칸에 도착하면 종료
    if num == 99:
            answer = cnt
            break
    
    # 다음으로 이동할 칸을 큐에 추가

    for dice_num in range(1, 7):
        new_num = num + dice_num

        # 칸을 벗어나는 경우는 무시
        if not(0<=new_num<100):
            continue
        
        if not visited[new_num]:
            # 뱀, 주사위칸에 도착한 경우 이동
            if mat[new_num] > 0:
                q.append([mat[new_num], cnt+1])
                visited[new_num] = True

        
            else:
                q.append([new_num, cnt+1])
                visited[new_num] = True


print(answer)