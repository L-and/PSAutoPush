import math

n, m = map(int, input().split())

answer = math.fabs(n-m)

print(int(answer))