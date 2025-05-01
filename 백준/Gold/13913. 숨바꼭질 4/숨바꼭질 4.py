from collections import deque
def find_k(n, k):

    ## not n <= k 일때 처리
    # N과 K가 같을때
    if n == k:
        return [0, [n]]
    #N이 K보다 클때
    elif n>k:
        return [n-k, list(range(n, k-1, -1))]

    node_queue = deque() # 생성된 노드들을 저장할 큐
    node_queue.append(n)
    generated[n] = 0 # 시작노드의 depth를 0으로 설정
    
    while len(node_queue) != 0: # 생성된 노드가 없을떄 까지 반복(k를 생성하면 생성을 그만둠)
        node = node_queue.popleft() # popleft
        
        if node == k:
            node_route = []
            last_node = k
            for i in range(generated[node]):
                node_route.append(last_node_list[last_node])
                last_node = last_node_list[last_node]

            node_route.insert(0, node)

            node_route = node_route[::-1]

            return [generated[node], node_route]

        # 규칙에 따라 새로운 노드 생성
        for new_node in [node-1, node+1, node*2]:
            # 0<=new_node<=100,000 범위 이내
            # 처음 생성된 노드를 큐에 추가(k라면 생성허용)
            if 0<=new_node<=100000 and generated[new_node] == not_gen:
                generated[new_node] = generated[node]+1
                node_queue.append(new_node)
                last_node_list[new_node] = node
            
    



n, k = map(int, input().split())
not_gen = -2
generated = [not_gen] * int(1e5+1) # generated[number] = depth(생성안된건 not_gen)
last_node_list = [0] * int(1e5+1)
fastest_data = find_k(n, k)

print(fastest_data[0])
print(*fastest_data[1])