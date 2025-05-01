from collections import deque

n = int(input())

adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = list(map(int, input().split()))

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

visited = [False for _ in range(n+1)]
q = deque()
q.append(1)
visited[1] = True

answer = [0 for _ in range(n+1)]

while q:
    p_node = q.popleft()
    
    for c_node in adj_list[p_node]:
        if not visited[c_node]:
            q.append(c_node)
            visited[c_node] = True

            answer[c_node] = p_node

for i in range(2, n+1):
    print(answer[i])