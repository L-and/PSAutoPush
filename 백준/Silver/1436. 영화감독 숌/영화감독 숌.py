n = int(input())
end_num = 666

while n != 0:
    if "666" in str(end_num):
        n -= 1
        if n == 0:
            break
        end_num += 1
    else:
        end_num += 1

print(end_num)