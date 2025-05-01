from math import factorial


n = int(input())

factoN = str(factorial(n)) # 팩토리얼한 숫자를 문자열로 저장

numLength = len(factoN)
zeroCount = 0
for i in range(len(factoN)): # 문자열의 뒷부분부터 검사
    if factoN[numLength - i - 1] != '0': # 0이 아닌숫자가 나오면 중단
        break

    zeroCount += 1

print(zeroCount)