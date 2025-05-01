from collections import deque

n = int(input())

mat = [[] for _ in range(n)]

for i in range(n):
    mat[i] = list(map(int,input().split()))


def bfs(start_node, end_node):
    visited = [False for _ in range(n)]
    q = deque()
    q.append(start_node)
    # visited[start_node] = True

    # print(f"I:{i}, J:{j}")
    while q:
        node = q.popleft()
        # print("Current Node: ",node)
        # print( mat[node], visited)
        for next_node, weight in enumerate(mat[node]):
            # print(next_node, visited[next_node])
            if weight == 1 and not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
                # print("\tNext Node: ", next_node)

    if visited[end_node]:
        return 1
    else:
        return 0
    
for i in range(n):
    for j in range(n):
        print(bfs(i, j),end=' ')
        
    print()