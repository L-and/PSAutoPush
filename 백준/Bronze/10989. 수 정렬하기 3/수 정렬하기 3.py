import sys

array_len = int(sys.stdin.readline())
counting_array = [0] * 10001
for i in range(array_len):
    counting_array[int(sys.stdin.readline())] += 1

for i in range(10001):
    if counting_array[i] != 0:
        for j in range(counting_array[i]):
            print(i)

