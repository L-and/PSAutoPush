from collections import deque

cmd_list=['L','R','D','S']

def trans(n, command):
    if command=='D':
        n = n * 2 % 10000

    elif command=='S':
        if n==0:
            n = 9999
        else:
            n -= 1

    elif command=='L':
        n = (n*10) % 10000 + (n//1000)
    elif command=='R':
        n = (n//10) + (n%10 * 1000)

    return n


t = int(input())

for _ in range(t):
    origin, target = map(int, input().split())

    predecessor = [[0, 0] for _ in range(10000)] # [new_num] = [num, last_cmd]

    # DSLR 연산을 origin에 수행하며 수행한 결과를 visited에 저장하며 BFS로 최소연산을 계산
    visited = [False for _ in range(10000)]

    # origin을 BFS 시작노드로 설정 및 방문처리
    q = deque()
    q.append(origin)
    visited[origin] = True

    while q:
        num = q.popleft()
        for cmd in cmd_list:
            new_num = trans(num, cmd)
            
            if not visited[new_num]:
                visited[new_num] = True
                q.append(new_num)
                predecessor[new_num] = [num, cmd]
    

        # visited[target] 이 True가 되면 predecessor[target]을 역추적하여 answer 생성
        if visited[target]:
            answer = ""
            predecessor[origin] = [None, None]
            tmp_num = predecessor[target]

            while tmp_num[0] != None:
                answer = tmp_num[1] + answer

                tmp_num = predecessor[tmp_num[0]]

            print(answer)
            break
        
                