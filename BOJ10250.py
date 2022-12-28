num = int(input())
for _ in range(num):
    h, w, n = map(int, input().split())
    result_floor = n % h
    result_room = n // h + 1
    if n % h == 0:
        result_room = n//h
        result_floor = h
    print(f'{result_floor*100+result_room}')