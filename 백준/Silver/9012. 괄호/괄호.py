def check_ves(ps):
    left_parentheses = 0  # 왼쪽 괄호
    right_parentheses = 0  # 오른쪽 괄호

    for i in range(len(ps)):
        parentheses = ps.pop(0)

        if parentheses == '(':
            left_parentheses += 1
        elif parentheses == ')':
            right_parentheses += 1

        if left_parentheses < right_parentheses:
            return False

    if left_parentheses == right_parentheses:
        return True
    else:
        return False


case = int(input())

for i in range(case):
    ps = list(input())

    if check_ves(ps):
        print("YES")
    else:
        print("NO")
