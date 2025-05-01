from collections import deque

n, m = map(int, input().split())

adj_list = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int,input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)
    

answer = 0
max_dist = 1000000

for i in range(n):
    depth = 0
    total_dist = 0
    nodes = [0 for _ in range(99)] # nodes[n] : Depth N의 노드 갯수

    visited = [False for _ in range(n)]

    q = deque()
    q.append(i)
    visited[i] = True
    nodes[depth] = 1

    while q:
        # print(nodes[depth])
        user = q.popleft()
        # print(f"User: {user+1} d: {depth}")
        # print(f"Node in Depth: {nodes[depth]}")
        nodes[depth] -= 1

        


        if nodes[depth] <= 0:
                depth += 1
                # print(f"[{user}] depth: {depth}")

            

        for u in adj_list[user]:
            if not visited[u]:
                q.append(u)
                visited[u] = True
                total_dist += depth
                
                nodes[depth+1] += 1
                
    # print(f"{i+1} answer : {total_dist}")
    if max_dist > total_dist:
        max_dist = total_dist
        answer = i+1
    

    

print(answer)
    

    