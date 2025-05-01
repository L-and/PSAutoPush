import sys


case = int(input())

pos = [None for pos_case in range(case)]

for i in range(case):
    pos[i] = list(map(int, sys.stdin.readline().split()))

pos.sort()

for i in range(case):
    print(pos[i][0], pos[i][1])