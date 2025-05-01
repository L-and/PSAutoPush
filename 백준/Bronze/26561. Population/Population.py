case = int(input())

for _ in range(case):
    p, t = map(int, input().split())

    p = p + t//4 - t //7

    print(p)
