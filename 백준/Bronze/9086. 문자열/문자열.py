n = int(input())

string_list = [0]*n

for i in range(0, n):
    string_list[i] = input()

for i in range(0, n):
    print(string_list[i][0],string_list[i][-1],sep='')