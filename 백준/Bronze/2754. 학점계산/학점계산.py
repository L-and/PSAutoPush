credit = input()

credit_dict = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}

credit_num = credit_dict[credit[0]]

if len(credit) >= 2:
    if credit[1] == '+':
        credit_num += 0.3
    elif credit[1] == '-':
        credit_num -= 0.3

print(credit_num)