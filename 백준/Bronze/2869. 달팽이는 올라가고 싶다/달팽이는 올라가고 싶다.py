from math import ceil

a, b, v= input().split()
a = int(a)
b = int(b)
v = int(v)

increase_value = a - b
v = v - b
answer = ceil(v / increase_value)
print(answer)