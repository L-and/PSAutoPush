test_case = int(input())

for case in range(test_case):
    items = dict()

    for i in range(int(input())):
        _, type = map(str, input().split())

        # 새로운 옷의 종류인경우
        if type not in items.keys():
            items[type] = 2 # 해당 옷과 아무것도 안입은경우, 즉 2로 초기화
        else:
            items[type] += 1

    combination = 1

    for value in items.values():
        combination *= value

    print(combination - 1) # 알몸인경우 1가지를 제외한값이 정답