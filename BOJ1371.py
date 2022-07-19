import sys

s = sys.stdin.read()
list1 = [0] * 26

for i in s:
    if i.islower():
        list1[ord(i) - 97] += 1

for i in range(26):
    if list1[i] == max(list1):
        print(chr(97 + i), end = '')