n = int(input())
test_score_list = list(map(int, input().split()))

max_score = max(test_score_list)
new_total = 0

for i in range(n):
    new_total = new_total + test_score_list[i] / max_score * 100

print(new_total / n)