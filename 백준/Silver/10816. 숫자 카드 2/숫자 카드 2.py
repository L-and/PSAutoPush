import sys

def lower_bound(array, target):
    low = 0
    high = len(array)

    while low < high:
        mid = (low + high) // 2
        if target <= array[mid]:
            high = mid
        else:
            low = mid + 1

    return low


def upper_bound(array, target):
    low = 0
    high = len(array)

    while low < high:
        mid = (low + high) // 2
        if target >= array[mid]:
            low = mid + 1
        else:
            high = mid

    return low


## 입력 ##

cardLength = sys.stdin.readline()

cardList = list(map(int, sys.stdin.readline().split()))

targetCardLength = int(sys.stdin.readline())

targetCardList = list(map(int, sys.stdin.readline().split()))

cardList.sort()  # binary search 를 사용하기위해 정렬

# countingValueList = [] # 이미 카운트 한 숫자를 저장
# countingValueCountList = [] # 이미 카운트 한 숫자의 수를 저장

# 결과 출력

for index, targetValue in enumerate(targetCardList):
    # if targetValue in countingValueList:
    #     print(countingValueCountList[countingValueList.index(targetValue)], end=' ')
    # else:
    targetCount = upper_bound(cardList, targetValue) - lower_bound(cardList, targetValue)

    # countingValueList.append(targetValue)
    # countingValueCountList.append(targetCount)

    print(targetCount, end=' ')
