import sys

K, L = map(int, sys.stdin.readline().split())

for i in range(2, L):
    if K % i == 0:
        print("BAD {}".format(i))
        exit()


print("GOOD")