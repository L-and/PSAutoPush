from collections import deque

n, m = map(int, input().split())

num_mat = [[] for _ in range(n)]
# mat[y][x]
for y in range(n):
    num_mat[y] = list(map(int, input().split()))

##############################

# 기본도형 5가지와 대칭하여 새로만들어지는 도형 2가지
base_tetromino_list = [
    [[0,0],[0,1],[0,2],[0,3]], # I
    [[0,0],[0,1],[1,0],[1,1]], # O
    [[0,0],[0,-1],[0,1],[1,0]], # T
    [[0,0],[1,0],[1,1],[2,1]], # S_1
    # [[0,0],[1,0],[1,-1],[2,-1]], # S_2
    [[0,0],[1,0],[2,0],[2,1]], # J_1
    # [[0,0],[1,0],[2,0],[2,-1]], # J_2
    ]

xy_reverse_list = []
for tetromino in base_tetromino_list:
    tmp = []
    for pos in tetromino:
        tmp.append([pos[1], pos[0]])

    xy_reverse_list.append(tmp)

base_tetromino_list += xy_reverse_list

# 대칭
flip = [[-1,1],[1,-1],[-1,-1]]

# 회전/ 대칭한 테트로미노 추가
tetromino_list = list()
for base in base_tetromino_list:
    tetromino_list.append(base)

    for oper in flip:
        new_tetromino = []
        for pos in base:
            new_tetromino.append([pos[0] * oper[0], pos[1] * oper[1]])
            
        if new_tetromino not in tetromino_list:
            tetromino_list.append(new_tetromino)

        new_tetromino = []
        for pos in base:
            new_tetromino.append([pos[1] * oper[0], pos[0] * oper[1]])
        
        if new_tetromino not in tetromino_list:
            tetromino_list.append(new_tetromino)

# print(*tetromino_list,sep='\n')
# print(len(tetromino_list))

max_value = -1
for pivot_y in range(n):
    for pivot_x in range(m):
        for tetro_pos_list in tetromino_list:
            tmp_sum = 0
            for tetro_pos in tetro_pos_list:
                x = pivot_x + tetro_pos[1]
                y = pivot_y + tetro_pos[0]

                # 범위검사
                if not(0<=x<m and 0<=y<n):
                    break

                tmp_sum += num_mat[y][x]
            
            if max_value < tmp_sum:
                max_value = tmp_sum
        
    

print(max_value)

