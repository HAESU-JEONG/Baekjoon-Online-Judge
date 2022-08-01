import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
card = list(map(int, sys.stdin.readline().rstrip().split()))

from itertools import combinations
combinations_list = list(combinations(card, 3))

sum_list = []

for i in range(len(combinations_list)):
    sum_card = combinations_list[i][0] + combinations_list[i][1] + combinations_list[i][2]
    if sum_card <= m:
        sum_list.append(sum_card)

print(max(sum_list))