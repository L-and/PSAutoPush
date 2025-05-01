a = map(int, input().split())
a = list(a)

add_value = a[0] - a[1]
for i in range(1, len(a) - 1):
    current_add_value = a[i] - a[i+1]
    if add_value != current_add_value:
        answer = 0
        current_add_value = 0
        break

if current_add_value == 1:
    answer = -1
elif current_add_value == -1:
    answer = 1

if answer == 1:
    print("ascending")
elif answer == -1:
    print("descending")
elif answer == 0:
    print("mixed")