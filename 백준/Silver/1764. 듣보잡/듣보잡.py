def binarySearch(targetWord:str, searchList:list, start:int, end:int) -> int:
    if start > end:
        return None

    mid = (start + end) // 2

    if searchList[mid] == targetWord:
        return mid
    elif searchList[mid] > targetWord: # 찾는 단어보다 mid의 단어가 크다면
        end = mid - 1
    elif searchList[mid] < targetWord: # 찾는 단어보다 mid의 단어가 작다면
        start = mid + 1

    return binarySearch(targetWord, searchList, start, end)

n, m = map(int, input().split()) # n : 듣도 못한 사람의 수, m : 보도 못한 사람의 수

hearWord = list() # 듣도 못한 사람
seeWord = list() # 보도 못한 사람
jobWord = list() # 듣보잡 사람(듣도 못한사람 ∩ 보도 못한 사람)

for i in range(n):
    hearWord.append(input())

for i in range(m):
    seeWord.append(input())

hearWord.sort()
seeWord.sort()

# 데이터입력 끝

for i in range(n):
    jobIndex = binarySearch(hearWord[i], seeWord, 0, m - 1)
    if jobIndex != None:
        jobWord.append(seeWord[jobIndex])
    
# 듣보잡의 명단구하기 끝

print(len(jobWord))
print(*jobWord, sep='\n')
