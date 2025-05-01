from math import gcd

num1 ,num2 = input().split()

num1 = int(num1)
num2 = int(num2)

gcd_num = gcd(num1, num2)
lcm_num = num1 * num2 // gcd_num

print(gcd_num)
print(lcm_num)