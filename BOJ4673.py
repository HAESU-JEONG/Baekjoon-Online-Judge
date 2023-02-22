natural_list = set(range(1, 10001))
generated_list = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_list.add(i)

self_num = sorted(natural_list - generated_list)
for i in self_num:
    print(i)