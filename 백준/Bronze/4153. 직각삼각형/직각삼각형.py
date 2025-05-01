from math import pow

length = map(int, input().split())
length = list(length)
length.sort()

while not(length[0] == 0 and length[1] == 0 and length[2] == 0):
    if pow(length[2], 2) == pow(length[0], 2) + pow(length[1], 2):
        print("right")
    else:
        print("wrong")

    length = map(int, input().split())
    length = list(length)
    length.sort()