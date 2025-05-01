def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())

A = list()

A = list(map(int, input().split()))

A.sort()

M = int(input())

B = list(map(int, input().split()))

for i in range(M):
    answer = binary_search(A, B[i], 0, N - 1)
    if answer == None:
        print(0)
    else:
        print(1)
