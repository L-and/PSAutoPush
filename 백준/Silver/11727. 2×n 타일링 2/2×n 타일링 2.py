n = int(input())

# tile[n] : 2*n 타일을 채우는 방법의 수
tile = [0 for i in range(1000+1)]

tile[1] = 1
tile[2] = 3

for i in range(3, n+1):
    tile[i] = tile[i-1] + 2*tile[i-2]

print(tile[n] % 10007)