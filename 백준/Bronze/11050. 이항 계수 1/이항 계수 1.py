from math import factorial

N, K = input().split()
N = int(N)
K = int(K)

answer = int(factorial(N)/(factorial(K) * factorial(N - K)))

print(answer)