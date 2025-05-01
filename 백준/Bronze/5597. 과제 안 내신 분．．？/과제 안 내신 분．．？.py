# 30명의 학생 중 과제를 내지않은 2명의 학생의 번호를 출력하는 문제

student_dict = {}

for i in range(30):
    student_dict[i] = 0

for i in range(28):
    n = int(input())
    student_dict[n - 1] = 1

for i in range(30):
    if student_dict[i] == 0:
        print(i + 1)
