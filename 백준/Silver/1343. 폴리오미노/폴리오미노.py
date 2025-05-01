s = input()

cnt = 0
answer = ""

for i, c in enumerate(s):
    if c == 'X':
        cnt += 1
    if c== '.' or (i == len(s) - 1):

        if cnt % 2 != 0:
            answer = -1
            break

        if cnt % 4 == 0:
            answer += "AAAA" * (cnt // 4)
            cnt = 0
        elif cnt % 4 == 2:
            answer += "AAAA"  * (cnt // 4) + "BB"
            cnt = 0

        if s[i] == '.':
            answer += '.'
        

print(answer)
