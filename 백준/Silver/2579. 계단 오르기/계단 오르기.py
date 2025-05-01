# 테스트케이스 입력값 처리
n = int(input())
score_list = [0]

for i in range(n):
    score_list.append(int(input()))

g = [0, 0] # 1계단 전으로부터 온 경우(1계단 이동)
h = [0, score_list[1]] # 2계단 전으로부터 온 경우(2계단 이동)

for i in range(2, n+1):
    g.append(h[i-1] + score_list[i])
    h.append(max(h[i-2], g[i-2]) + score_list[i])

print(max(h[n], g[n]))