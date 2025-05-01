num = input()

while num != '0':
    half_len_of_num = int(len(num) / 2)

    answer = 1

    for i in range(half_len_of_num):
        if num[i] != num[len(num) - i - 1]:
            answer = 0
            break
        answer = 1

    if answer == 1:
        print("yes")
    elif answer == 0:
        print("no")

    num = input()