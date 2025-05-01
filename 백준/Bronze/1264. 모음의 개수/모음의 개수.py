vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input().lower()

    if s == "#":
        break

    cnt = 0
    for v in vowels:
        for c in s:
            if v == c:
                cnt += 1

    print(cnt)