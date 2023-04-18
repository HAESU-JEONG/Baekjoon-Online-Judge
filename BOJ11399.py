people = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
result = 0

for i in range(people+1):
    result += sum(num_list[0:i])
print(result)