score = []
for _ in range(8):
    score.append(int(input()))

score_sorted = sorted(score, reverse=True)
big5 = []
for i in range(5):
    big5.append(score_sorted[i])

tmp = []
sum_score = 0
for i in big5:
    sum_score += i
    tmp.append(score.index(i))
print(sum_score)
tmp.sort()
for i in tmp:
    print(i + 1, end = " ")