while True:
    n = int(input())
    length = int(input())
    if n <= 100 and length <= 10000:
        break

string = input()

P = []

for i in range(n):
    P.append('I')
    P.append('O')
P.append('I')
p_string = ''.join(P)

cnt = 0
for i in range(length):
    if string.find(p_string) != -1:
        index = string.find(p_string)
        string = ''.join(string[index + 1:])
        cnt += 1

print(cnt)