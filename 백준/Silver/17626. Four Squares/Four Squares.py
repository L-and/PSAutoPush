import math

def calcDp(num):
    for i in range(1, math.isqrt(num)+1):
        if(dp[num] == 0):
            dp[num] = dp[i*i] + dp[num-i*i]
        else:
            dp[num] = min(dp[num], dp[i*i] + dp[num-i*i])

n = int(input())

# dp[n] : n을 dp[n]개의 제곱수 합으로 표현가능하다는 뜻
dp = [0 for i in range(50000+1)]

# 제곱수의 경우는 미리 1로 정의(1,4,9,16 이런 i*2인것들)
# 범위가 Root n인 것은 예를를들어 n이 25인경우 i를 5까지만 계산해도 25 즉 1로 답이 나오기 때문
for i in range(1, math.isqrt(n)+1):
    dp[i*i] = 1


for i in range(1,n+1):
    if dp[i] != 0: # 위의 식으로 계산된건 무시
        continue

    calcDp(i) # 이 식으로 dp[i]를 모조리 채워서 마지막 dp[n]을 구함

print(dp[n])