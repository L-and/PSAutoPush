import sys


class Deque:
    def __init__(self):
        self.data = list()

    def push_front(self, x):
        self.data.insert(0, x)

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        if not self.empty():
            return self.data.pop(0)
        else:
            return -1

    def pop_back(self):
        if not self.empty():
            return self.data.pop(-1)
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


deque = Deque()

case = int(input())

for i in range(case):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        deque.push_front(command[1])
    elif command[0] == "push_back":
        deque.push_back(command[1])
    elif command[0] == "pop_front":
        print(deque.pop_front())
    elif command[0] == "pop_back":
        print(deque.pop_back())
    elif command[0] == "size":
        print(deque.size())
    elif command[0] == "empty":
        print(deque.empty())
    elif command[0] == "front":
        print(deque.front())
    elif command[0] == "back":
        print(deque.back())