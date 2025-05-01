n = int(input())

x_pos_list = list()
y_pos_list = list()

for i in range(n):
    x, y = map(int, input().split())
    
    x_pos_list.append(x)
    y_pos_list.append(y)

width = max(x_pos_list) - min(x_pos_list)
height = max(y_pos_list) - min(y_pos_list)

print(width * height)