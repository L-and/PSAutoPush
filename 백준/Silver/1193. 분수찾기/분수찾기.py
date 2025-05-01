n = int(input())

line = 0
tmp_n = 0

while n > tmp_n:
    line = line + 1
    tmp_n = tmp_n + line

if line % 2 == 0:
    print(line + 1 - ( tmp_n - n + 1 ),'/', tmp_n - n + 1, sep='')
elif line % 2 == 1:
    print(tmp_n - n + 1,'/',line + 1 - ( tmp_n - n + 1 ), sep='')