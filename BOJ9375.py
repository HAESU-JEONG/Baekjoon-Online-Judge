from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)
    wear_cnt = Counter(wear)
    cnt = 1

    for key in wear_cnt:
        cnt *= wear_cnt[key] + 1
    print(cnt - 1)