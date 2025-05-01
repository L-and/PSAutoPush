num_list_len = int(input())
num_list = list()

for i in range(num_list_len):
    num_list.append(int(input()))

num_list = sorted(num_list)

for i in range(num_list_len):
    print(num_list[i])
