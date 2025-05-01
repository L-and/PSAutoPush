ary = list()
number = list()
stack = list()
push_pop_stack = list()
end = False
i = 1

n = int(input())
for j in range(n):
    number.append(int(input()))

for j in range(n):
    while number[j] >= i:
        push_pop_stack.append("+")
        stack.append(i)
        i += 1

    push_pop_stack.append("-")
    if stack.pop() != number[j]:
        print("NO")
        end = True
        break

if not end:
    for i in push_pop_stack:
        print(i)

