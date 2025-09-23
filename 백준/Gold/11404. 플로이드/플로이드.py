n = int(input()) # 도시(노드)의 수
m = int(input()) # 버스(간선)의 수

INF = int(1e9)
adj = [[INF] * (n+1) for _ in range((n+1))] # 간선의 연결정보를 저장할 인접행렬

for _ in range(m):
    a, b, cost = map(int, input().split())

    # 노선의 비용이 작은경우에만 저장(시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.)
    adj[a][b] = min(cost, adj[a][b])
    adj[a][a] = 0 # A도시에서 A로 가는경우 비용을 0으로 설정

# 플로이드 마샬
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

# 그래프 출력
for i in adj[1:]:
    for cost in i[1:]:
        if cost == INF:
            print("0", end=' ') # 노선이 없는경우 0을 출력
        else:
            print(cost, end=' ')
    print()