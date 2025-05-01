num_of_words = int(input())

words = list()
words_length = set()

for i in range(num_of_words):
    word = input()
    words.append(word)
    words_length.add(len(word))

row = max(words_length)

sorted_words = [[] for M in range(row)]
sorted_words_set = [[] for M in range(row)]


for i in range(num_of_words):
    sorted_words[len(words[i]) - 1].append(words[i])

for i in range(row):
    sorted_words_set[i] = set(sorted_words[i])
    sorted_words[i] = list(sorted_words_set[i])

for i in range(row):
    sorted_words[i].sort()

for i in range(len(sorted_words)):
    for j in range(len(sorted_words[i])):
        print(sorted_words[i][j])