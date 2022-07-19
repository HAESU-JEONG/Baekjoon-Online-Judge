num = int(input())
string = input()
x = [int(a) for a in str(string)]

result = 0
for i in range(num):
    result = result + x[i]

print(result)