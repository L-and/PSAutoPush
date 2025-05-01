# A: 2명
# B: 4명
# C: 5명

# 총 감독관의 감시가능 인원: 1명
# 부 감독관의 감시가능 인원: 2명

# 각 시험장마다 필요한 감독관의 수: 총 감독관 1명 + 부 감독관 n명
# (Ai - B) / c =  n
import math
n = int(input())

a = list(map(int, input().split()))

b, c = map(int, input().split())

total_proctor_cnt = 0
for i in range(n):
    a[i] -= b # 총 감독관이 감시가능한 인원 제외 후 감독관 카운트 증가
    total_proctor_cnt += 1

    if a[i] >= 1: # 시험장에 감독이 필요한 인원이 남았는가?
        total_proctor_cnt += math.ceil(a[i] / c)

print(total_proctor_cnt)