import sys

def my_round(num:float):
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)

n = int(sys.stdin.readline())

level_voting_list = list()
for i in range(n):
    level_voting_list.append(int(sys.stdin.readline()))

if n==0:
    answer = 0
else:
    level_voting_list.sort() # 나중에 절삭평균을 하기위해 정렬

    del_num = my_round(n * 0.15)

    level_voting_list = level_voting_list[del_num:n-del_num]

    answer = my_round(sum(level_voting_list) / (n - del_num*2))

print(answer)