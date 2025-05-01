n = int(input())
position = list()

for i in range(n):
    position.append(list(map(int, input().split())))

position.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(position[i][0], position[i][1])