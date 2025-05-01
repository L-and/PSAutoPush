N, r, c = map(int, input().split())

# ex)N=2, r=3, c=1
# 단계는 n까지 존재함
# 각 단계마다 r과 c를 이용하여 찾는 숫자의 범위(사분면)을 줄여나가는 방식으로 탐색

# 각 사분면은 Z모양으로 세아려 짐
# 아래의 수식은 각 단계를 실행 후 다음 단계에서 계산
# 1사분면이면 r,c는 유지
# 2사분면이면 c-=2^n
# 3사분면이면 r-=2^n
# 4사분면이면 r-=2^n, c-=2^n

# 1단계
# r=3, c=1이므로 찾는 숫자는 3사분면에 존재함
# 2단계
# r=3, c=1
result = 0
for n in range(N, 0, -1):
    m = (2**n - 1) // 2

    if r <= m and c <= m:
        result += 0
    elif r <= m and c > m:
        result += 4**(n-1)
        c-=2**(n-1)
    elif r > m and c <= m:
        result += 2*4**(n-1)
        r-=2**(n-1)
    elif r > m and c > m:
        result += 3*4**(n-1)
        r-=2**(n-1)
        c-=2**(n-1)

print(result)
