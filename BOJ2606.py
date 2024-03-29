computer = int(input())
pair = int(input())

graph = [[] * computer for _ in range(computer + 1)]
for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (computer + 1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)