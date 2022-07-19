p = ['pi', 'ka', 'chu']
string = input()
total = 0

for i in p:
    total += string.count(i) * len(i)

if total == len(string):
    print("YES")
else:
    print("NO")