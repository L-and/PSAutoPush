k = int(input()) # k개의 정수가 주어짐

stack = list() # 입력받은 값을 저장할 스택리스트


for i in range(k):
    tmp = int(input()) # 값을 임시로 입력받음
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)

print(sum(stack))