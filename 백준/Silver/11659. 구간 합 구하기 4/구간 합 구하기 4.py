import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

### 누적합 배열 생성
prefix_sum_num_list = [num_list[0]]

for index in range(1, len(num_list)):
    prefix_sum_num_list.append(prefix_sum_num_list[index-1] + num_list[index])
###

for _ in range(m):
    start, last = map(int, sys.stdin.readline().split())
    
    start -=1
    last -=1
    
    if start-1 < 0:
        result = prefix_sum_num_list[last]
    else:
        result = prefix_sum_num_list[last] - prefix_sum_num_list[start-1]

    print(result)