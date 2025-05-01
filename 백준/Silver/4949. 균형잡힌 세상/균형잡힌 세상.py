input_list = list()

tmp = input()
parenthesis_stack = list() # 다음 입력되어야할 괄호를 저장할 스택

while tmp != "." : # . 이 입력되기전까지 입력받은 값을 input_list 에 추가
    input_list.append(tmp)
    tmp = input()

for string in input_list: # input_list 의 문자열을 하나씩 string 으로 저장

    balance = True

    for character in string: # string 의 각 문자를 character 에 저장\

        # character 이 여는괄호면 다음에 와야하는 괄호를 parenthesis_stack 에 저장
        if character == '(':
            parenthesis_stack.append(')')
        elif character == '[':
            parenthesis_stack.append(']')

        # character 이 닫는괄호면 다음에 와야하는 괄호가 맞는지 검사
        if character == ')' or character == ']':
            if len(parenthesis_stack) != 0: # parenthesis_stack 이 비어있으면 다음에 올 괄호가 있으면 안된다는뜻
                if character != parenthesis_stack.pop(): # 괄호가 틀렸으면 균형이 깨졌으므로 False 를 저장 후 반복문 탈출
                    balance = False
                    break
            else:
                balance = False
                break

    if len(parenthesis_stack) != 0: # parenthesis_stack 이 안비어있다는뜻은 괄호가 안닫혔다는 뜻
        balance = False
        
    parenthesis_stack.clear() # 다음문자열을 검사하기위해 초기화

    # 균형이 맞다면 yes 틀리다면 no 출력
    if balance is True:
        print("yes")
    else:
        print("no")
