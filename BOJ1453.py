person_cnt = int(input())
seat_want = list(map(int, input().split()))
seat = [0 for _ in range(100)]
result = 0
for s in seat_want:
    if seat[s - 1] != 0:
        result += 1
    else: seat[s - 1] += 1

print(result)