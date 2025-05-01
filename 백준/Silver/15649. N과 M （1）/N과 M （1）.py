# bfs를 써서 1~n까지 root를 설정한 뒤 자식노드들을 부모노드.append(1~n중 부모노드에 없는 숫자)를 하며 len이 m인거까지 만들고
# len:m을 모두 출력하면 답이 아닐까?

n, m = map(int, input().split())

v = [False for _ in range(n+1)]
s = []

def dfs():
    if len(s) == m:
        print(*s, sep=' ')
        return 
    
    for i in range(1, n+1):
        if not v[i]:
            v[i] = True
            s.append(i)
            dfs()
            s.pop(-1)
            v[i] = False

dfs()