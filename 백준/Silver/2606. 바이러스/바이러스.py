# 그래프를 dict로 저장 후 BFS

pc_count = int(input())
edges_count = int(input())

graph = {}
for i in range(1, pc_count+1):
    graph[i] = []

for i in range(edges_count):
    node1, node2 = map(int, input().split())
    
    graph[node1] = graph[node1] + [node2]
    graph[node2] = graph[node2] + [node1]

############## 여까지 입력 #######################
worm_count = 0 # 감연된 PC의 수

visited = [] # 방문 한 노드 저장
queue = [1] # 방문 할 노드 저장

# print(graph)
while len(queue) != 0: # 큐가 빌떄까지 반복
    selected_node = queue.pop(0) # 방문 할 노드 꺼냄

    # 방문 안 한 노드라면 방문처리
    if selected_node not in visited:
        visited.append(selected_node)
    else: # 방문햇으면 다음 방문할 노드로 ㄱㄱ
        continue

    # selected_node와 연결된 노드들을 큐에 저장
    for node in graph[selected_node]:
        if node not in visited:
            queue.append(node)
    

    worm_count += 1  
    # print(visited)
    # print(selected_node)

print(worm_count - 1) # 1번 PC는 포함X이므로 -1해서 출력