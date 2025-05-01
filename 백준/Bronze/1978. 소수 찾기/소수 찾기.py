def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                 return False
        return True

N = int(input())

prime_count = 0

num = list(map(int, input().split()))

for i in range(N):
    if isPrime(num[i]):
        prime_count = prime_count + 1

print(prime_count)