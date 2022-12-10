a, b = map(int, input().split())

num_list = [0]

for i in range(1, b+1):
    for j in range(i):
        num_list.append(i)

result = 0
for i in range(a, b+1):
    result += num_list[i]
print(result)