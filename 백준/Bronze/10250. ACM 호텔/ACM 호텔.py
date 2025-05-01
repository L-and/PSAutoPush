case = int(input())

for i in range(case):
    height, width, n = input().split()
    height = int(height)
    width = int(width)
    n = int(n)

    room = [[0 for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            room[i][j] = (i + 1) * 100 + (j + 1)

    current_n = 0
    current_height = 0
    current_width = 0

    while current_n < n - 1:
        if current_height < height - 1:
            current_n = current_n + 1
            current_height = current_height + 1
        elif current_height == height - 1:
            current_n = current_n + 1
            current_height = 0
            current_width = current_width + 1
        # print(current_height, current_width, current_n)
        # input()
    
    print(room[current_height][current_width])