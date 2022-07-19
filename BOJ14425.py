N, M = map(int, input().split())
origin = []
test = []

for i in range(N):
    origin.append(input())

for j in range(M):
    test.append(input())

count = 0

for i in range(N):
    count += test.count(origin[i])

print(count)