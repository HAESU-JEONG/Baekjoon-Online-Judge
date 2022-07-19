def count(s):
    c = 1
    max_c = 1
    compare = s[0]

    for i in s[1:]:
        if i == compare:
            c += 1
        else:
            max_c = max(max_c, c)
            compare = i
            c = 1
    max_c = max(max_c, c)
    return max_c

for i in range(3):
    print(count(input()))