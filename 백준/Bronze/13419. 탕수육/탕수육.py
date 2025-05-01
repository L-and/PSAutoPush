t = int(input())

for _ in range(t):
    word = input()
    
    answer = ["", ""]
    if len(word) == 1:
        answer[0] = word
        answer[1] = word
    else:
        for i in range(0, len(word), 2):
            answer[0] += word[i]

        for i in range(1, len(word), 2):
                    answer[1] += word[i]

        if len(word)%2 == 1:
            for i in range(1, len(word), 2):
                answer[0] += word[i]

            for i in range(0, len(word), 2):
                answer[1] += word[i]

    print(answer[0])
    print(answer[1])