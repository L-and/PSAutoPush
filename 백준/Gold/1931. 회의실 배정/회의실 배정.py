# 도움된 사이트
# https://hongcoding.tistory.com/22
# https://st-lab.tistory.com/145

n = int(input()) # 회의의 갯수
t = []

for i in range(n):
    t.append(list(map(int, input().split())))

t.sort(key = lambda x:x[0])
t.sort(key = lambda x:x[1])

count = 1
end = t[0][1] # 맨 처음으로 끝나는시간을 기준으로 잡아줌

for i in range(1, n): 
    if end <= t[i][0]: # 끝나자고 가장빠르게 시작되는 회의가 있다면
        count +=1 # 카운트를 높이고
        end = t[i][1] # 회의종료시간을 갱신해줌

print(count)