answer = [0, 1, 2, 4]

def answerCount(num):
    if len(answer) <= num:
        for i in range(len(answer), num+1):
            answer.append(answer[i-1] + answer[i-2] + answer[i-3])

    return answer[num]



t = int(input())

for i in range(t):
    n = int(input())

    print(answerCount(n))
    

# Case:
#     1 : 1가지(1)
#     2 : 2가지(1+1, 2)
#     3 : 4가지(1+1+1, 1+2, 2+1, 3)
#     4 : 7가지(1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1)
#     5 : 13가지(1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+1+2, 2+2+1, 1+2+2, 3+1+1, 1+3+1, 1+1+3, 3+2, 2+3)

# 결론: num의 결과 = (num-1)의 결과+(num-2)의결과+(num-3)의 결과