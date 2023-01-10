import sys
from collections import Counter

n, m, inven = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n): graph += map(int, sys.stdin.readline().split())
height, time = 0, 1000000000000000

min_h = min(graph)
max_h = max(graph)
_sum = sum(graph)
graph = dict(Counter(graph))

for i in range(min_h, max_h + 1):
    if _sum + inven >= i * n * m:
        cur_time = 0
        for key in graph:
            if key > i:
                cur_time += (key - i) * graph[key] * 2
            elif key < i:
                cur_time += (i - key) * graph[key]
        if cur_time <= time:
            time = cur_time
            height = i

print(time, height)