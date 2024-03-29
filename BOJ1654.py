import sys
k, n = map(int, input().split())
lan_list = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan_list)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan_list:
        lines += i // mid
    
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)