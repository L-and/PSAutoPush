from collections import deque

que = deque()

N = int(input())

for i in range(N):
    que.append(i+1)

while len(que) != 1:
    que.popleft()
    que.append(que.popleft())

print(que.pop())
