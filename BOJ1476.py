e, s, m, cnt = 1, 1, 1, 1
i_e, i_s, i_m = map(int, input().split())

while True:
    if i_e == e and i_s == s and i_m == m:
        break
    e += 1
    s += 1
    m += 1
    cnt += 1
    if e >= 16:
        e -= 15
    if s >= 29:
        s -= 28
    if m >= 20:
        m -= 19

print(cnt)