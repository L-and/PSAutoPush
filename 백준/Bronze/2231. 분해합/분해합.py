def check_generator_num(checked_num): # 1 : 생성자O ,0 : 생성자X
    checked_num_length = len(str(checked_num))

    str_checked_num = str(checked_num)

    total_digit_sum = 0

    for i in range(checked_num_length):
        total_digit_sum = total_digit_sum + int(str_checked_num[i])
    

    if num == checked_num + total_digit_sum:
        return 1
    else:
        return 0

num = int(input())

for generator_num in range(num // 2, num):
    if check_generator_num(generator_num):
        break

    generator_num = 0
    
print(generator_num)

