from math import pow
distinguished_num = map(int, input().split())
distinguished_num = list(distinguished_num)

answer = 0

for i in range(len(distinguished_num)):
    answer = answer + pow(distinguished_num[i],2)

answer = int(answer % 10)

print(answer)