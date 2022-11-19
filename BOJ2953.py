score_list = [[0] * 4 for _ in range(5)]
total_list = [0] * 5

for i in range(5):
    score_list[i] = list(map(int, input().split()))
    total_list[i] = sum(score_list[i])

max_score = max(total_list)
for i in range(5):
    if total_list[i] == max_score:
        print(i+1, max_score)