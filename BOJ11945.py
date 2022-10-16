n, m = map(int, input().split())

for i in range(n):
    s = list(input())
    result = reversed(s)
    print(''.join(result))