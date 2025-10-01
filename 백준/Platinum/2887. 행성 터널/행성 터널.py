# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input()) # 행성의 개수
pos = [] # (x, y, z, 행성번호) 튜플형태로 위치저장
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    pos.append((x, y, z, i))

# 간선을 저장할 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# x, y, z좌표기준으로 정렬한 후, 인접한 행성끼리의 터널(간선)을 생성해 줌 (3 * (n-1)개의 간선 생성)
for axis in range(3):
    pos.sort(key=lambda item: (item[axis]))
    for i in range(n-1):
        cost = abs(pos[i+1][axis] - pos[i][axis])
        edges.append((cost, pos[i][3], pos[i+1][3]))

edges.sort()

# 부모 테이블 초기화
parent = [0] * (n+1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 비용순으로 정렬된 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
    
print(result)