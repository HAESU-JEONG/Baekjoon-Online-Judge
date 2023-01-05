num = int(input())
honeycomb = 1
result = 1

while num > honeycomb:
    honeycomb += 6 * result
    result += 1
print(result)