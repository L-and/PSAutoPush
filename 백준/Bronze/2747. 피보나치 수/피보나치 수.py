def fibonacci(n):
    answer = 0 
    next = 1

    for _ in range(n):
        answer, next = next, answer + next
    
    return answer

n = int(input())

print(fibonacci(n))