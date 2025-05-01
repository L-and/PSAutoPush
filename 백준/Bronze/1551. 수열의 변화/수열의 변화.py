n, k = map(int,input().split())

num_list = list(map(int,input().split(',')))

for _ in range(k):
    tmp_list = []

    for i in range(len(num_list)-1):
        tmp_list.append(num_list[i+1] - num_list[i])

    num_list = tmp_list

print(*num_list,sep=',')