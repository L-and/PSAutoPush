import heapq

t = int(input())
for _ in range(t):
    k = int(input())

    maxh = []
    minh = []
    trace = dict()

    for _ in range(k):
        cmd, num = map(str, input().split())
        num = int(num)

        # print(cmd, num)
                
        if cmd == 'I':
            heapq.heappush(maxh, -num)
            heapq.heappush(minh, num)

            if num in trace.keys():
                trace[num] += 1
            else:
                trace.update({num: 1})

        elif cmd == 'D':
            if len(trace) > 0:
                if num == 1 and len(maxh) > 0:
                    while not -maxh[0] in trace.keys():
                        heapq.heappop(maxh)

                    p_val = -heapq.heappop(maxh)
                elif num == -1 and len(minh) > 0:
                    while not minh[0] in trace.keys():
                        heapq.heappop(minh)

                    p_val = heapq.heappop(minh)

                # print("p_val:",p_val)
                if trace[p_val] > 1:
                    trace[p_val] -= 1
                elif trace[p_val] == 1:
                    del trace[p_val]

        # print(trace)
        # print("min:", minh,"\nmax:", maxh, '\n')


    if len(maxh) > 0:
        while not -maxh[0] in trace.keys():
            heapq.heappop(maxh)
            if len(maxh) == 0:
                break

    if len(minh) > 0:
        while not minh[0] in trace.keys():
            heapq.heappop(minh)
            if len(minh) == 0:
                break
    
    if len(maxh) > 0 and len(minh) > 0:
        b_val = -heapq.heappop(maxh)
        s_val = heapq.heappop(minh)

        print(b_val, s_val)
    else:
        print("EMPTY")