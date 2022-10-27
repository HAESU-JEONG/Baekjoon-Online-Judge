n, m = map(int, input().split())

if m < n and m < 3:
    print("NEWBIE!")
elif (m < n or m == n) and m > 2:
    print("OLDBIE!")
else:
    print("TLE!")