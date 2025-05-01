def makenewnum(num, p):
    new_num = 0
    for i in range(len(num)):
        new_num += int(num[i]) ** p

    return new_num


a, p = input().split()
p = int(p)

d = [int(a)]

newNum = makenewnum(str(a), p)

while newNum not in d:
    d.append(newNum)
    newNum = makenewnum(str(d[-1]), p)

print(d.index(newNum))