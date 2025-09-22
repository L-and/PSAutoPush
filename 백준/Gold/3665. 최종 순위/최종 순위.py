from collections import deque

t = int(input())

for _ in range(t):
    v = int(input()) # 팀의 수
    rank = list(map(int, input().split())) # 작년 순위

    # 노드의 진입차수를 0으로 초기화
    indegree = [0] * (v + 1)

    # 각 노드의 간선을 저장할 그래프
    graph = [[] for i in range(v + 1)]

    # i등 노드로 1 ~ (i-1)등 팀의 노드에서 간선이 이어지도록 그래프를 초기화
    # 즉, 진입차수가 많을수록 순위가 낮다는 의미
    for i in range(v):
        a = rank[i]
        for j in range(i+1, v):
            b = rank[j]
            graph[a].append(b) # A에서 B로 이동가능

            # B의 진입차수를 1 증가
            indegree[b] += 1

    # 위상정렬
    def topology_sort():
        result = [] # 결과를 담을 리스트
        q = deque()

        # 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, v + 1):
            if indegree[i] == 0:
                q.append(i)

        # 큐가 빌때까지 반복
        while q:
            # 큐에서 노드 꺼내기
            now = q.popleft()
            result.append(now)

            # 꺼낸 노드와 연결된 노드의 진입차수를 1 빼줌
            for i in graph[now]:
                indegree[i] -= 1

                # 진입차수가 0이된 노드를 큐에 추가
                if indegree[i] == 0:
                    q.append(i)

        
        # 데이터에 일관성이 없음 (사이클이 생김)
        if len(result) != v:
            print("IMPOSSIBLE", end=' ')
        else:
            # 랭킹순(진입차수가 적은 노드순)으로 팀번호 출력
            for i in result:
                print(i, end=' ')
        
        print()

    # 올해 순위정보 입력
    m = int(input())

    # 작년 순위정보 간선 갱신
    for _ in range(m):
        a, b = map(int, input().split())
        
        if a in graph[b]:
            # b에서 a로가는 간선이 있을경우
            graph[b].remove(a) # 간선 제거
            indegree[a] -= 1 # 진입차수 갱신

            graph[a].append(b) # 간선 연결
            indegree[b] += 1 # 진출차수 갱신
        elif b in graph[a]: 
            # a에서 b로가는 간선이 있을경우
            graph[a].remove(b) # 간선 제거
            indegree[b] -= 1 # 진입차수 갱신

            graph[b].append(a) # 간선 연결
            indegree[a] += 1 # 진출차수 갱신

    # 위상정렬 시작
    topology_sort()
