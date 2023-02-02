import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)