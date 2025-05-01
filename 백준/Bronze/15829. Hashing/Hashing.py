from math import pow

l = int(input())
str_key = input()
int_key = []

hash_value = 0

M =  1234567891

for i in range(l):
    int_key.append(ord(str_key[i]) - ord('`'))          # 입력값을 정수로 변환
    hash_value = hash_value + int_key[i] * 31 ** i   # 입력값을 해쉬값으로 변환

print(hash_value % M)