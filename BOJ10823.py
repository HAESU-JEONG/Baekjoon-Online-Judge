import sys
data = list(map(int, sys.stdin.readline().split(',')))
result = 0
for i in range(len(data)):
    result += data[i]
print(result)