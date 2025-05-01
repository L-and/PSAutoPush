# 단어를 입력받아 대소문자를 바꿔 출력하는 문제

word = list(input())

for i in range(len(word)):
    if word[i].islower():
        word[i] = word[i].upper()
    else:
        word[i] = word[i].lower()

print("".join(word))