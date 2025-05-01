sentence = input()

# "009" 와 같은 수에서 00을 제외하기 위해 이전에 +,-가 등장하였는지를 저장하는 변수
prev_is_operator = True
normalized_sentence = "" # 의미없는 0을 제거한 식을 저장할 변수
temp = 0 # 숫자를 char에서 int로 바꾸기 위한 임시변수

# 입력값에서 의미없는 0을 제거
# list에 수를 int로 저장 및 기호를 '+','-' 로 저장
for char in sentence:
    # char이 +,-이면 다음char이 0일경우 제외를 위해 True로 설정
    if char == '+' or char == '-':
        prev_is_operator = True
        normalized_sentence += char
        temp = 0 # 다음 수를 저장하기위해 이전수 초기화
    # 이전 char이 +,- 이었으며 현재 char이 0인경우 숫자 앞에 의미없는 0이므로 저장X
    elif prev_is_operator and char == '0':
        continue
    # char이 0이 아닌경우 이후char이 제거되지 않아야 하니 False로 설정
    else:
        prev_is_operator = False
        normalized_sentence += char

normalized_sentence = normalized_sentence.split('-')

for i in range(len(normalized_sentence)):
    normalized_sentence[i] = eval(normalized_sentence[i])

answer = normalized_sentence[0]

for i in range(1, len(normalized_sentence)):
    answer -= normalized_sentence[i]

print(answer)
