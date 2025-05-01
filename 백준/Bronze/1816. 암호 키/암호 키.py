n = int(input())

for _ in range(n):
    small = False
    key = int(input())
    for i in range(2, int(1e6)+2):
        
        if key % i == 0:
            small = True
            break
            
    if small:
        print("NO")
    else:
        print("YES")