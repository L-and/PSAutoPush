h, m = map(int, input().split())
oven_m = int(input())

m += oven_m

h += m//60
h = h%24
m = m%60

print(h, m)