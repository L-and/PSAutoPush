x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

distance = [w - x, x, h - y, y]

distance.sort()

print(distance[0])