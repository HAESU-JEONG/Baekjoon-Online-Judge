import sys

n = int(sys.stdin.readline().rstrip())
num_list = [0] * 10001

for _ in range(n):
    index = int(sys.stdin.readline().rstrip())
    num_list[index] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
