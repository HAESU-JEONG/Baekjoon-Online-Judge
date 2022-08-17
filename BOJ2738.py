import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix1 = []

for i in range(n):
    matrix1.append(list(map(int, input().split())))

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        matrix1[i][j] += temp[j]

for i in range(n):
    for j in range(m):
        print(matrix1[i][j], end = " ")
    print()