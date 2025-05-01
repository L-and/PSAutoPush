n = int(input())

num_dict = {}

for i in range(-100, 101, 1): # 딕셔너리의 키를 -100~100 범위로 설정
  num_dict[i] = 0

num_list = list(map(int, input().split())) # 수를 입력받고 그 수의 개수를 딕셔너리의 value로 저장

for i in range(n): # 수를 입력받고 그 수의 개수를 딕셔너리의 value로 저장
    num_dict[num_list[i]] += 1

v = int(input()) # 찾으려고하는 정수 v를 입력받음

print(num_dict[v])