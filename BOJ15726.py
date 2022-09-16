a, b, c = map(int, input().split())
result = []

result.append((a/b)*c)
result.append((a*b)/c)

print(int(max(result)))