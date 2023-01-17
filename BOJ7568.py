num = int(input())
data = []
result = []

for i in range(num):
    weight, height = map(int, input().split())
    data.append([weight, height])

for i in range(num):
    cnt = 0
    for j in range(num):
        if i == j:
            continue
        else:
            if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
                cnt += 1
    result.append(cnt + 1)

for i in range(num):
    print(result[i])