def get_rank(user_data_list, index):
    rank = 0
    for i in range(len(user_data_list)):
        if i == index:
            continue

        compare_count = 0
        for j in range(2): # 몸무게와 키 비교
            if user_data_list[i][j] > user_data_list[index][j]:
                compare_count += 1

        if compare_count == 2:
            rank += 1

    return rank+1


userNum = int(input())
userDataList = list()

for i in range(userNum):
    userDataList.append(list(map(int, input().split())))

for i in range(userNum):
    print(get_rank(userDataList, i), end=' ')
