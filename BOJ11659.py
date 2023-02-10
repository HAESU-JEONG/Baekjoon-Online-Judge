import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pfs_list = list(map(int, input().split()))
for i in range(n-1):
    pfs_list[i+1] += pfs_list[i]
pfs_list = [0] + pfs_list

for _ in range(m):
    a, b = map(int, input().split())
    print(pfs_list[b] - pfs_list[a-1])