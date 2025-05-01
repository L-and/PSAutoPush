p = [0,1,1,1]

case_cnt = int(input())

for _ in range(case_cnt):
    n = int(input())
    
    for i in range(len(p), n+1):
        p.append(p[i-2] + p[i-3])

    print(p[n])