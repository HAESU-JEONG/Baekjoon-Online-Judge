n, k = map(int, input().split())
coin_list = []

for i in range(n):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)

answer = 0
for i in coin_list:
    if k == 0:
        break
    answer += k//i
    k %= i
print(answer)