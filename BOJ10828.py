import sys
input=sys.stdin.readline

class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if (not self.items) == True:
            return -1
        else:
            return self.items.pop()
    def isEmpty(self):
        return not self.items
    def top(self):
        if (not self.items) == True:
            return -1
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)

stk = stack()
num = int(input().strip())
for i in range(num):
    string = list(input().strip().split())
    if string[0] == "push":
        stk.push(string[1])
    elif string[0] == "pop":
        print(stk.pop())
    elif string[0] == "size":
        print(stk.size())
    elif string[0] == "empty":
        if stk.isEmpty() == True:
            print(1)
        else:
            print(0)
    elif string[0] == "top":
        print(stk.top())