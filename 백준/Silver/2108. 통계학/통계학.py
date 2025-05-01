# 통계학

num_list = list()  # 입력값들을 저장할 리스트

n = int(input())  # num 의 개수를 저장

# n 개의 num 을 입력받아 num_list 에 저장
for i in range(n):
    num_list.append(int(input()))

num_list.sort()  # 입력받은 값을 올림차순으로 정렬

# 1. 산술평균
print(round(sum(num_list) / len(num_list)))

# 2. 중앙값
middle_index = len(num_list) // 2  # 중앙값의 인덱스
print(num_list[middle_index])

# 3. 최빈값
frequency_dict = dict()  # 각 수의 빈도수를 저장할 딕셔너리[num, frequency]


def f1(x):
    return frequency_dict[x]


for value in num_list:
    if value not in frequency_dict.keys():  # value 가 frequency_dict 에 없으면
        frequency_dict[value] = 0  # 생성해준다

    frequency_dict[value] += 1  # 빈도수를 1씩 추가

max_frequency_cnt = max(frequency_dict.values())  # 최대 빈도수를 저장

max_frequency_dict = dict(filter(lambda item:item[1]==max_frequency_cnt, frequency_dict.items()))  # value 가 최대 빈도수인
# 딕셔너리 생성

cnt_list = list(max_frequency_dict.keys())  # 위에서 만든 딕셔너리에서 value 를 리스트로 저장

# 최빈값이 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
if len(cnt_list) >= 2:
    print(cnt_list[1])
else:
    print(cnt_list[0])


# 4. 범위
min_num = min(num_list)
max_num = max(num_list)

print(max_num - min_num)
