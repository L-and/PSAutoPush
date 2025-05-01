import sys

n, m, b = map(int, sys.stdin.readline().split())
y = list()
for i in range(n):
    y.append(list(map(int, sys.stdin.readline().split())))

# 브루투포스로 0~256 모든범위 다 돌려서 제일작은 time 찾기
max_time = 100000000
answer_time = 1000000000
answer_y = 0

for target_y in range(257):
    low = 0
    high = 0
    time = 0
    for i in range(n):
        for j in range(m):
            if y[i][j] > target_y:
                high += (y[i][j] - target_y)  # target_y 보다 높은블럭을 더하기
            elif y[i][j] < target_y:  # target_y 보다 낮은곳을 채우기
                low += (target_y - y[i][j])  # target_y 보다 낮은블럭을 더하기

    time = low + high * 2

    current_b = b + high  # 현재 인벤토리의 블럭 수
    # 인벤토리 블럭수가 쌓아야할 블럭보다 적으면 시간을 100만으로 설정후 break
    if current_b < low:
        time = max_time
        break

    if time < max_time and time <= answer_time:
        answer_time = time
        answer_y = target_y


print(answer_time, answer_y)
