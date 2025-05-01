card_num, max_num = input().split()
card_num = int(card_num)
max_num = int(max_num)

card = map(int, input().split())
card = list(card)

current_sum = 0
max_sum = 0

for i in range(card_num):
    for j in range(i + 1, card_num):
        for k in range(j + 1, card_num):
            current_sum = card[i] + card[j] + card[k]
            if current_sum > max_sum and current_sum <= max_num:
                max_sum = current_sum

print(max_sum)