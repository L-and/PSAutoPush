import sys


class Stack:
    def __init__(self):
        self.data = list()

    def push(self, x):
        self.data.append(x)

    def pop(self):
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

    def top(self):
        if self.empty():
            return -1
        else:
            return self.data[-1]


stack = Stack()

case = int(input())

for i in range(case):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stack.push(command[1])
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())