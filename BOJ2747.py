import sys

fibo = [0, 1]
n = int(sys.stdin.readline())
for i in range(2, n + 1):
    fibo.append(fibo[i - 1] + fibo[i - 2])
print(fibo[-1])