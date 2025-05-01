from enum import Enum
class Size(Enum):
    S = 0
    M = 1
    L = 2
    XL = 3
    XXL = 4
    XXXL = 5

n = int(input())
size_list = list(map(int, input().split()))
t, p = map(int, input().split())

t_result = 0

for size in size_list:
    if size % t > 0:
        t_result += size // t + 1
    else:
        t_result += size // t

p_result = n // p
p_single_result = n % p

print(t_result)
print(p_result, p_single_result)