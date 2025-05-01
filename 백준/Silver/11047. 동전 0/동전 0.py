# 1. 동전의 종류중 K원보다 높은것들은 제거
# 2. K -= N[-1]
# 1~2 반복하면 될듯?

n, k = list(map(int, input().split()))
coinValue = list()
count = 0

for i in range(n):
    coinValue.append(int(input()))

coinValue = list(filter(lambda x: x <= k, coinValue))

while True:
    if k == 0:
        break

    
    
    count += k // coinValue[-1]
    k %= coinValue[-1]

    for i in reversed(range(len(coinValue))):
        if k < coinValue[i]:
            del coinValue[i]

print(count)