num_list = []

for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    num_list.append(score)

avg = sum(num_list) / 5
print(int(avg))