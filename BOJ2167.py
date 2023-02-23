n, m = map(int, input().split())
num_list = []
dp = [[0] * (m+1) for _ in range(n+1)]

for _ in range(n):
    num_list.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = num_list[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])