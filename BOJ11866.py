import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
num_list = deque([i+1 for i in range(n)])
print("<", end="")

for i in range(n):
    for j in range(k - 1):
        num_list.append(num_list.popleft())
    print(num_list.popleft(), end="")
    if i != n - 1:
        print(", ", end='')
print(">")