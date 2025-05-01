n = int(input())

len_s = int(input())
s = input()

count = 0
index = 0
sub_count = 0
while index < len_s:
    if s[index:index+3] == "IOI":
        sub_count = 0
        index += 2
        sub_count += 1
        if sub_count >= n:
                count += 1
                sub_count -= 1
        while s[index:index+3] == "IOI":
            index +=2
            sub_count += 1

            if sub_count >= n:
                count += 1
                sub_count -= 1
    else:
        index += 1
    

print(count)