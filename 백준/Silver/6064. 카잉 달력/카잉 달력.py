import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    answer = -1
    year = x
    while year < math.lcm(n, m) + 1:
        maya_x = year % (m)
        maya_y = year % (n)
        if maya_x == 0:
            maya_x = m
        if maya_y == 0:
            maya_y = n

        if [x, y] == [maya_x, maya_y]:
            answer = year
            break

        year += m
    
    print(answer)
