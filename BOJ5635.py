n = int(input())
person_list = []

for _ in range(n):
    name, day, month, year = input().split()
    person_list.append([int(year), int(month), int(day), name])

person_list.sort(key = lambda x: (x[0], x[1], x[2]))
print(person_list[n-1][3])
print(person_list[0][3])