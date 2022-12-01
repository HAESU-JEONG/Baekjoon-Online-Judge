num = int(input())
result = "%.300f" % (1 / pow(2, num))

length = len(result)

for i in range(len(result) - 1, 1, -1):
    if result[i] != '0':
        length = i + 1
        break

print(result[:length])