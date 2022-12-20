n, k = map(int, input().split())
weight_list = [0]
profit_list = [0]

for i in range(n):
    weight, profit = map(int, input().split())
    weight_list.append(weight)
    profit_list.append(profit)

result_list = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < weight_list[i]:
            result_list[i][j] = result_list[i-1][j]
        else:
            result_list[i][j] = max(result_list[i-1][j], result_list[i-1][j - weight_list[i]] + profit_list[i])

print(result_list[n][k])