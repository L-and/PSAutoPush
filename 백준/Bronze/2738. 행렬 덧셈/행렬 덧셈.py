# n*m 크기의 두 행렬을 더해서 결과를 출력하는 문제

n, m = map(int, input().split())

A = [[0 for j in range(m)] for i in range(n)]
B = [[0 for j in range(m)] for i in range(n)]
answer = [[0 for j in range(m)] for i in range(n)]

# 입력
for i in range(n):
        A[i] = list(map(int, input().split()))

for i in range(n):
    B[i] = list(map(int, input().split()))

# 계산
for i in range(n):
    for j in range(m):
        answer[i][j] = A[i][j] + B[i][j]

# 출력
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()
