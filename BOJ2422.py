import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
ice = [[False for _ in range(n)] for _ in range(n)]

for i in range(m):
    ice1, ice2 = map(int, input().split())
    ice[ice1 - 1][ice2 - 1] = True
    ice[ice2 - 1][ice1 - 1] = True

result = 0

for i in combinations(range(n), 3):
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    result += 1
print(result)