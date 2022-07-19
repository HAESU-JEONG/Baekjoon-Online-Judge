import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(str, input().split())

    temp1 = sorted(list(a))
    temp2 = sorted(list(b))

    if temp1 == temp2:
        print(a + " & " + b + " are anagrams.")

    else:
        print(a + " & " + b + " are NOT anagrams.")