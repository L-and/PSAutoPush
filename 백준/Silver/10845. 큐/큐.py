import sys


class Queue:
    def __init__(self):
        self.data = list()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.empty():
            return self.data.pop(0)
        else:
            return -1

    def size(self):
        return len(self.data)

    def empty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.data[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.data[-1]


queue = Queue()

case = int(input())

for i in range(case):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.push(command[1])
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "empty":
        print(queue.empty())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "back":
        print(queue.back())