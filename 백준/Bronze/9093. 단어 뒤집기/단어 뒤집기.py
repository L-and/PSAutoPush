# 1. 공백을 기준으로 문자열을 분리
# 2. 모든 문자열들을 거꾸로 뒤집음

n = int(input())

for i in range(n):
    s = input()

    s_list = s.split()
    
    for i in range(len(s_list)):
        s_list[i] = s_list[i][::-1]

    print(' '.join(s_list))