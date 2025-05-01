n, k = map(int, input().split())

num_queue = list(range(1, n + 1))
killed_list = list()
count = 0
kill_count = 0

while kill_count != n:
    num_queue.append(num_queue.pop(0))
    count += 1

    if count == k:
        killed_list.append(str(num_queue.pop(-1)))
        count = 0
        kill_count += 1

print('<'+', '.join(killed_list)+'>')
