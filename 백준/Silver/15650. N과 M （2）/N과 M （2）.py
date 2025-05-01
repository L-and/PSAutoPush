n, m = map(int, input().split())

v = [False for _ in range(n+1)]

node = []

def dfs(node):
    if len(node) == m:
        print(*node, sep=' ')
        return
    
    for i in range(1, n+1):
        if v[i]:
            continue
        
        if len(node) == 0:
            pass
        else:
            if i<node[-1]:
                continue
        node.append(i)
        v[i] = True
        dfs(node)
        node.pop(-1)
        v[i] = False

dfs(node)
