n, m = map(int, input().split())
n_string = str(n)
nm = ''

while len(nm) < len(n_string) * n:
    nm += n_string
print(nm[:m])